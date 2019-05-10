FROM python:3.7-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /code

COPY . /code/

RUN pip install -r requirements.txt
#CMD export DJANGO_PASSWORD=$(cat /etc/secrets/djangouserpw); gunicorn -b :$PORT mysite.wsgi

