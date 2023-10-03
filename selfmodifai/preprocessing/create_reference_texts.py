import re
import csv
from transformers import pipeline

def create_reference_texts():
    with open("data/brittanica_b1.txt") as f:
        brittanica_b1 = f.read()
    
    texts_clean = re.split(r'\n{2,}', brittanica_b1.strip())


    with open('data/reference_texts.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        
        counter = 0   
        for text in texts_clean:
            if 284 < len(text) < 844 and re.search(r"[a-zA-Z]", text):
                counter += 1
                writer.writerow([text])
        
        print(counter)

