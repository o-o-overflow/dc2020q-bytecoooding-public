FROM python:3.7-alpine

ENV TERM linux


# For example:
run apk update && apk add --no-cache netcat-openbsd bash g++ make openssl-dev libffi-dev
COPY requirements.txt /requirements.txt
run pip install -r requirements.txt

RUN mkdir /solutions
COPY solutions /solutions

COPY exploit1.sh /
COPY check1.py /
