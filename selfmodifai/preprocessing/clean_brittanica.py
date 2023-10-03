import re


def clean_brittanica():
    with open("data/brittanica.txt") as f:
        brittanica = f.read()[:1115394]

    brittanica_clean = re.sub(r"\n+", "\n", brittanica)

    with open("data/brittanica_clean.txt", "w") as f:
        f.write(brittanica_clean)
