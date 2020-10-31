FROM python:3

USER root

ENV PYTHONUNBUFFERED 1

ENV PORT 8080

RUN mkdir /code

WORKDIR /app

ADD . /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app
