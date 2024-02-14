FROM python:3.10.7

RUN mkdir -p '/user/src/app'
WORKDIR '/user/src/app'

ENV PYTHONDONTWRITEBYTECODE = 1
ENV PYTHONUNBUFFERED=1

RUN pip install --upgrade pip

COPY . /user/src/app

RUN pip install -r requirements.txt
