import re
import openai


def team_agent():
    brainstormer_messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Create an artificial neural network architecture for text generation that no one has thought of yet",
        },
    ]
    brainstormer_response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=brainstormer_messages)
    brainstromer_response_content = brainstormer_response["choices"][0]["message"]["content"]
    print("Brainstormer: ", brainstromer_response_content)

    # Pattern to match code blocks
    pattern = r"```(\w+)\n(.*?)```"

    contains_code = re.search(pattern, brainstromer_response_content, re.DOTALL)

    if contains_code:
        print("\nBrainstormer contains code")

    else:
        new_messages = [
            {"role": "assistant", "content": brainstromer_response_content},
            {"role": "user", "content": "Write the code for this in PyTorch"},
        ]
        engineer_messages = brainstormer_messages + new_messages
        engineer_response = openai.ChatCompletion.create(model="gpt-4", messages=engineer_messages)
        engineer_response_content = engineer_response["choices"][0]["message"]["content"]
