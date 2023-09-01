import json


def conv_history_to_str(self, messages, full_context, user_name="user", assistant_name="assistant"):
    for message in messages[1:]:
        if message["role"] == "user":
            role = user_name
        elif message["role"] == "assistant":
            role = assistant_name

        content = message["content"]

        full_context += f"{role}: {content}\n\n"

    return full_context


def update_messages(content, role, messages, messages_file):
    new_message = {"role": role, "content": content}
    messages.append(new_message)
    with open(messages_file, "w") as outfile:
        json.dump(messages, outfile)

    step = f"Step: {content}"
    print(step)

    with open("logs.txt", "a") as f:
        f.write(step)

    return messages
