# pull official base image
FROM python:3.8.1-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat && \
    rm -rf /var/lib/apt/lists/*

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY *.py requirements.txt entrypoint.sh /usr/src/app/
COPY migrations/ /usr/src/app/migrations/
COPY postavljalec_vejic// /usr/src/app/postavljalec_vejic/
COPY bert_model_naucen /usr/src/app/bert_model_naucen/
COPY crosloengual-bert-pytorch/ /usr/src/app/crosloengual-bert-pytorch/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
