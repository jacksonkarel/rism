# syntax=docker/dockerfile:1

FROM huggingface/transformers-pytorch-gpu

WORKDIR /selfmodifai

COPY requirements.txt selfmodifai/requirements.txt

COPY setup.py selfmodifai/setup.py

COPY README.md selfmodifai/README.md

COPY selfmodifai selfmodifai/selfmodifai

COPY prompts selfmodifai/prompts

RUN pip install ./selfmodifai 

WORKDIR /selfmodifai/model

CMD ["tail", "-f", "/dev/null"]