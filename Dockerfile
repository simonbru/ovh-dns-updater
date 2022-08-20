FROM python:3.10-slim-bullseye

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN mkdir /code
WORKDIR /code
USER nobody
