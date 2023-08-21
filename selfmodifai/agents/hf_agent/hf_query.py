import json
import requests
import os


def hf_query(payload, api_url):
    HF_TOKEN = os.environ.get("HF_TOKEN")
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    data = json.dumps(payload)
    response = requests.request("POST", api_url, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))
