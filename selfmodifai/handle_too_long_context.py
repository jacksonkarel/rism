import openai
from openai.error import InvalidRequestError

def handle_too_long_context(messages):
    print("too long context")
    messages = messages[:-1]
    full_context = "Condense the information from the following past conversation between us. Keep all of the information that is relevant to the task at hand and remove all that is not:\n"
    for message in messages[1:]:
        role = message["role"]
        content = message["content"]

        full_context += (f"{role}: {content}\n\n")

    print(full_context)
    system_turn = {'role': 'system', 'content': 'You are part of an agent that is modifying the code of the model Alpaca-LoRA. The agent is in the Alpaca-LoRA directory. When you write code, that code will be executed and the output will be sent back to you.'}

    less_messages = [system_turn, {'role': 'user', 'content': full_context}]

    try:
        response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=less_messages
                )
        less_messages = [system_turn, {'role': 'assistant', 'content': response["choices"][0]["message"]["content"]}]

    except InvalidRequestError as e:
            # Check if the error message matches the context length issue
            if "maximum context length" in str(e):
                 response, less_messages = handle_too_long_context(messages)

            else:
                # Re-raise the exception if it's not what we're looking for
                raise e

    return response, less_messages