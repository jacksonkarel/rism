from huggingface_hub import InferenceClient


def llama_algo_gen():
    client = InferenceClient(
        "meta-llama/Meta-Llama-3.1-70B-Instruct",
        token="hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
    )

    for message in client.chat_completion(
        messages=[{"role": "user", "content": "What is the capital of France?"}],
        max_tokens=500,
        stream=True,
    ):
        print(message.choices[0].delta.content, end="")