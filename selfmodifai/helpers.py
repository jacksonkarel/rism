from openai import OpenAI

client = OpenAI()


def openai_response(model, messages):
    response = client.chat.completions.create(model=model, messages=messages)
    response_content = response["choices"][0]["message"]["content"]

    return response_content
