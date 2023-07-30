# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /selfmodifai

RUN apt-get -y update

RUN apt-get -y upgrade

RUN apt-get -y install git

RUN git clone https://github.com/jacksonkarel/selfmodifai

RUN pip install ./selfmodifai

WORKDIR /selfmodifai/model

CMD ["tail", "-f", "/dev/null"]