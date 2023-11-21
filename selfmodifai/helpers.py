import openai


def openai_response(model, messages):
    response = openai.ChatCompletion.create(model=model, messages=messages)
    response_content = response["choices"][0]["message"]["content"]

    return response_content
