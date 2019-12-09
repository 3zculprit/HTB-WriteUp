FROM python:3.6-alpine

RUN pip install flask
RUN pip install flask-restplus
RUN pip install Flask-SQLAlchemy
RUN pip install pymysql 
RUN pip install pyjwt
RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev
RUN pip install cryptography


WORKDIR /opt/app
EXPOSE 8888