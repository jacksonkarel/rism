import re
import openai
from transformers import pipeline
from selfmodifai.agents.fine_tunable_agents.team_agent.helpers import code_from_gpt


def team_agent():
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Create an artificial neural network architecture for text generation that no one has thought of yet that attempts to be very good at generalization",
        },
    ]
    brainstorm_response = openai.ChatCompletion.create(model="gpt-3.5-turbo-1106", messages=messages)
    brainstorm_response_content = brainstorm_response["choices"][0]["message"]["content"]
    print("Brainstorm: ", brainstorm_response_content)

    # Pattern to match code blocks
    pattern = r"```(\w+)\n(.*?)```"

    contains_code = re.search(pattern, brainstorm_response_content, re.DOTALL)

    if contains_code:
        print("\nBrainstormer contains code")

    else:
        new_messages = [
            {"role": "assistant", "content": brainstorm_response_content},
            {"role": "user", "content": "Write the code for this in PyTorch"},
        ]
        messages += new_messages
        engineer_response = openai.ChatCompletion.create(model="gpt-4", messages=messages)
        engineer_response_content = engineer_response["choices"][0]["message"]["content"]

        print("Engineer: ", engineer_response_content)

        code_files = code_from_gpt(engineer_response_content)

        if code_files:
            manager_messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": f"Is this code complete?",
                },
            ]

            complete_code = ""

            for code in code_files:

                code_content = code[1]

                classifier = pipeline("zero-shot-classification")
                labels = [
                    "complete",
                    "incomplete",
                ]
                results = classifier(
                    sequences=code_content,
                    candidate_labels=labels,
                    hypothesis_template="This text says that the code is {}",
                )

                result_label = results["labels"][0]

                if result_label == "complete":
                    complete_code += code_content

                else:
                    print("Incomplete code: ", code_content)
                    break
        else:
            print("No code detected")
