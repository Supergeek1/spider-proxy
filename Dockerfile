FROM python:3.7-stretch

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

WORKDIR /app
COPY . /app
RUN pip3 install -U pip && pip3 install -r requirements.txt
CMD python run.py