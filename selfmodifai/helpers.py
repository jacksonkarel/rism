from openai import OpenAI


def openai_response(model, messages, log_title):
    client = OpenAI()
    response = client.chat.completions.create(model=model, messages=messages)
    response_content = response.choices[0].message.content

    print(f"{log_title}:\n", response_content)

    return response_content


def openai_r_and_update(model, messages, log_title):
    response_content = openai_response(model, messages, log_title)
    messages.append(response_content)
    return response_content, messages


def new_openai_message(message, log_title):
    messages = [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": message}]
    response_content = openai_response("gpt-4", messages, log_title)

    return response_content


def new_openai_mru(model, message, messages, log_title, update_messages=True):
    message_data = {"role": "user", "content": message}
    messages.append(message_data)
    response_content = openai_response(model, messages, log_title)

    if update_messages:
        messages.append({"role": "assistant", "content": response_content})

    return response_content, messages
