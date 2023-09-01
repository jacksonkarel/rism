import replicate


def llama2_replicate():
    output = replicate.run(
        "a16z-infra/llama-2-7b-chat:7b0bfc9aff140d5b75bacbed23e91fd3c34b01a1e958d32132de6e0a19796e2c",
        input={"prompt": ...},
    )
    # The a16z-infra/llama-2-7b-chat model can stream output as it's running.
    # The predict method returns an iterator, and you can iterate over that output.
    for item in output:
        # https://replicate.com/a16z-infra/llama-2-7b-chat/versions/7b0bfc9aff140d5b75bacbed23e91fd3c34b01a1e958d32132de6e0a19796e2c/api#output-schema
        print(item)
