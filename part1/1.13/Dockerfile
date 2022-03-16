FROM golang:1.16.8-buster

EXPOSE 8080

WORKDIR /usr/src/app

COPY . .

RUN go build

RUN ./server
