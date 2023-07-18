import openai
from selfmodifai.gpt4_agent.helpers import conv_history_to_str


def handle_too_long_context(messages):
    print("too long context")
    messages = messages[:-1]
    full_context = "Condense the information from the following past conversation between us. Keep all of the information that is relevant to the task at hand and future important tasks and remove all that is not. Keep information about the locations of newly created files that might be helpful for future tasks. Imagine a future person picking up where you left off based on this summary. Please by fairly detailed. The past conversation:\n"

    full_context = conv_history_to_str(messages, full_context)

    print(full_context)
    system_turn = {
        "role": "system",
        "content": "You are part of an agent that is modifying the code of the model Alpaca-LoRA. The agent is in the Alpaca-LoRA directory. When you write code, that code will be executed and the output will be sent back to you.",
    }

    less_messages = [system_turn, {"role": "user", "content": full_context}]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=less_messages,
    )

    print(response["choices"][0]["message"]["content"])
    print(response["usage"]["total_tokens"])

    less_messages = [system_turn, {"role": "assistant", "content": response["choices"][0]["message"]["content"]}]

    return response, less_messages
