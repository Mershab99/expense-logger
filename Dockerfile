FROM python:3.8

ENV PYTHONBUFFERED=1

RUN mkdir /code
WORKDIR /code
ADD . /code/

RUN pip install -r requirements.txt
EXPOSE 8000 5432