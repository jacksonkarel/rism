import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

class TextGenerationModel:
    def __init__(self, model_path):
        self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        self.model = GPT2LMHeadModel.from_pretrained('gpt2')
        self.model.load_state_dict(torch.load(model_path))
        self.model.eval()
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model.to(self.device)
    
    def generate_text(self, input_text, max_length=50):
        with torch.no_grad():
            input_ids = self.tokenizer.encode(input_text, return_tensors='pt').to(self.device)
            output_ids = self.model.generate(input_ids, max_length=max_length)
            generated_text = self.tokenizer.decode(output_ids[0], skip_special_tokens=True)
        return generated_text
