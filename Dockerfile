FROM python:3.8-slim

WORKDIR /srv
COPY ./ /srv

RUN pip install --no-cache-dir -e .[dev]
