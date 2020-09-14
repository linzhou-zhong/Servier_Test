FROM python:3.7
MAINTAINER Linzhou "linzhou.zhong@efrei.net"
ENV STRINGS_INPUT="ab,abc,ab"
COPY . /code
WORKDIR /code
EXPOSE 5000
RUN pip3 install -r config/requirements.txt
WORKDIR /code/algorithme
ENTRYPOINT ["python3","-m","main"]
