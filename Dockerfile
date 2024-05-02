FROM python:3.11-slim

RUN mkdir /codes

COPY ./* /codes/

RUN apt-get update && apt-get install nano

RUN pip install "fastapi[all]" uvicorn pytest

WORKDIR /codes