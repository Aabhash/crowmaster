FROM python:3.7-slim

RUN apt-get update

RUN apt-get install enchant -y

RUN apt-get install gcc -y

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

RUN python -m nltk.downloader punkt

RUN python -m spacy download en_core_web_sm

COPY . /app

RUN pip install -e .

RUN python -m src.bot.bot