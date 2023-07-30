from transformers import AutoModelForCausalLM, AutoConfig, AutoTokenizer
import torch


def falcon_40b_generate(input_text):
    model_path = "tiiuae/falcon-40b-instruct"

    config = AutoConfig.from_pretrained(model_path, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_path, trust_remote_code=True, load_in_4bit=True, device_map="auto"
    )

    tokenizer = AutoTokenizer.from_pretrained("tiiuae/falcon-40b-instruct")

    input_ids = tokenizer(input_text, return_tensors="pt").input_ids.to("cuda")

    outputs = model.generate(input_ids, max_length=100)
    return tokenizer.decode(outputs[0])
