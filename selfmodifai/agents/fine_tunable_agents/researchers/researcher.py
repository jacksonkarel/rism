import replicate


def researcher():
    llama2_model_version = "meta/llama-2-70b-chat:02e509c789964a7ea8736978a43525956ef40397be9033abf9fd2badfe68c9e3"
    with open("prompts/from_scratch/better_than_transformer.txt", "r") as f:
        prompt = f.read()

    output = replicate.run(
        llama2_model_version,
        input={
            "prompt": prompt,
            "max_tokens": 5000,
            "system_prompt": "You are a helpful and honest assistant. Always answer as helpfully as possible. If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.",
        },
    )
    output_str = "".join(output)
    print("Llama 2:\n", output_str)
