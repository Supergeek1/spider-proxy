FROM tiangolo/meinheld-gunicorn-flask:python3.7

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

WORKDIR /app
COPY . /app
RUN pip3 install -r requirements.txt -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com