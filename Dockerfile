FROM python:3.11-slim

RUN mkdir /codes

COPY ./* /codes/

RUN apt-get update && apt-get install nano

# RUN pip install "fastapi[all]" uvicorn pytest
RUN pip install --no-cache-dir -r /codes/requirements.txt

WORKDIR /codes