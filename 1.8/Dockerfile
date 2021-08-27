FROM ubuntu:18.04

WORKDIR /usr/src/app

COPY curler.sh .

RUN chmod +x curler.sh

RUN apt-get update; apt-get install curl -y

CMD ./curler.sh