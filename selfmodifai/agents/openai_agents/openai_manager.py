import openai


def openai_manager(messages):
    for message in messages:
        if message["role"] == "user":
            message["role"] = "assistant"

    messages[-1][
        "content"
    ] += "\n\n What's a next step I can take to create a better model architecture than the transformer?"

    manager_sys_prompt = "You are keeping an AI language model that is trying to create a better model architecture than transformers on track."

    messages.insert(0, {"role": "system", "content": manager_sys_prompt})

    manager_response = openai.ChatCompletion.create(model="gpt-4", messages=messages)

    content = manager_response["choices"][0]["message"]["content"]

    print(f"Manager: {content}")

    return content
