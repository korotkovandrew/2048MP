FROM python:latest

RUN apt-get update && apt-get install -y \
    python3-dev \
    python3-pip \
    build-essential

WORKDIR /server

COPY . /server

RUN pip install -r requirements.txt
