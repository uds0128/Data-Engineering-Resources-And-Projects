FROM ubuntu:latest

RUN apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install python3 python3-pip net-tools openjdk-11-jdk procps -y && \
    pip3 install pyspark notebook pandas && \
    mkdir -p /src

COPY init.sh /init.sh

CMD ["bash", "/init.sh"]
