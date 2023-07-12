# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /selfmodifai

RUN apt-get -y update

RUN apt-get -y upgrade

RUN apt-get -y install git

RUN git clone https://github.com/jacksonkarel/selfmodifai

RUN pip install ./selfmodifai

RUN git clone https://github.com/jacksonkarel/selfmodifai-alpaca-lora.git

WORKDIR /selfmodifai/selfmodifai-alpaca-lora

CMD ["/bin/bash"]