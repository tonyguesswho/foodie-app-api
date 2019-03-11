# base image
FROM python:3.7-alpine

# maintainer
LABEL maintainer="Anthony Ugwu <anthony.uguw@andela.com>"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D user
USER user

#######
