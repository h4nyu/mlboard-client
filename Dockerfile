FROM python:3.8-alpine AS prod

WORKDIR /srv
COPY ./ /srv

RUN apk update \
    && apk add --no-cache gcc libc-dev openssl-dev libffi-dev inotify-tools \
    && pip install --no-cache-dir -e .[dev] \
    && apk del gcc libc-dev openssl-dev libffi-dev
