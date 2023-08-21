import requests


def llama2_hf_api():
    API_URL = "https://api-inference.huggingface.co/models/meta-llama/Llama-2-7b-chat-hf"
    headers = {"Authorization": "Bearer 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"}

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()

    output = query(
        {
            "inputs": "Can you please let us know more details about your ",
            "parameters": {
                "max_new_tokens": 250,
            },
        }
    )
    print(output)
