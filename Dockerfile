# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /selfmodifai

COPY selfmodifai selfmodifai

COPY requirements.txt requirements.txt

COPY setup.py setup.py

COPY README.md README.md

RUN pip install .

RUN apt-get -y update

RUN apt-get -y upgrade

RUN apt-get -y install git

RUN git clone https://github.com/jacksonkarel/selfmodifai-alpaca-lora.git

WORKDIR /selfmodifai/selfmodifai-alpaca-lora

COPY messages.json messages.json

CMD ["/bin/bash"]