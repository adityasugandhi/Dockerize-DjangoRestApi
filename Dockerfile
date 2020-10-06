FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /django-crud
WORKDIR /django-crud
COPY . /django-crud/
RUN pip install -r requirements.txt

