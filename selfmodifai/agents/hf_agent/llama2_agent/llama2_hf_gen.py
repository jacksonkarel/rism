import os
import json
import requests


def llama2_hf_gen():
    data = {"inputs": "What's the algorithm behind GPT-2?"}
    HF_TOKEN = os.environ.get("HF_TOKEN")
    headers = {"Authorization": f"Bearer {HF_TOKEN}", "Content-Type": "application/json"}

    LLAMA2_HF_ENDPOINT = os.environ.get("LLAMA2_HF_ENDPOINT")
    response = requests.post(LLAMA2_HF_ENDPOINT, headers=headers, data=json.dumps(data))
    print(response.json())
