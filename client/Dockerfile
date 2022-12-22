FROM python:latest


RUN apt-get update && apt-get install -y \
    python3-dev \
    python3-pip \
    build-essential \
    libnss3 \
    python3-pyqt5

RUN pip install pyqt5 

WORKDIR /client

COPY . /client
