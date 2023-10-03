import csv
import torch
import nltk
from nltk.translate.bleu_score import sentence_bleu
from nltk.translate.meteor_score import meteor_score
from rouge import Rouge


def generate_from_string(input_str, model, device, encode, decode, max_new_tokens=2000):
    input_tensor = torch.tensor(encode(input_str), dtype=torch.long, device=device).unsqueeze(0)
    output_tensor = model.generate(input_tensor, max_new_tokens=max_new_tokens)
    output_str = decode(output_tensor[0].tolist())
    return output_str


def auto_eval(model, device, encode, decode):
    # If using NLTK for the first time, download additional resources
    nltk.download("wordnet")

    # Load evaluation dataset
    with open("reference_texts.csv", "r") as file:
        reader = csv.reader(file)
        evaluation_data = list(reader)

    # Initialize lists to store scores
    bleu_scores = []
    meteor_scores = []
    rouge_scores = []

    rouge = Rouge()

    # Iterate over evaluation dataset and compute scores
    for row in evaluation_data[:10]:
        reference = row[0].lower()
        # Adjust depending on your CSV structure
        candidate = generate_from_string(reference, model, device, encode, decode)  # Generate prediction using the PyTorch model

        # Compute BLEU score
        bleu = sentence_bleu([reference.split()], candidate.split())
        bleu_scores.append(bleu)

        # Compute METEOR score
        meteor = meteor_score([reference.split()], candidate.split())
        meteor_scores.append(meteor)

        # Compute ROUGE score
        rouge_score = rouge.get_scores(candidate, reference, avg=True)
        rouge_scores.append(rouge_score)

    # Calculate average scores
    avg_bleu = sum(bleu_scores) / len(bleu_scores)
    avg_meteor = sum(meteor_scores) / len(meteor_scores)
    avg_rouge = {
        metric: sum([score[metric]["f"] for score in rouge_scores]) / len(rouge_scores)
        for metric in ["rouge-1", "rouge-2", "rouge-l"]
    }

    # Output results
    print(f"Average BLEU Score: {avg_bleu}")
    print(f"Average METEOR Score: {avg_meteor}")
    print(f"Average ROUGE Scores: {avg_rouge}")
