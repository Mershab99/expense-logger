FROM python:3.9
ENV PYTHONBUFFERED=1

RUN pip install flask flask_restful flask-cors flask-sqlalchemy flask-migrate psycopg2-binary

RUN mkdir /code
ADD . /code/
WORKDIR /code/


EXPOSE 80

ENTRYPOINT ["python"]
CMD ["./run.py"]

