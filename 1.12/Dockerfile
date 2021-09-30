FROM node:14

EXPOSE 5000

RUN curl -sL https://deb.nodesource.com/setup_14.x | bash

RUN  apt install -y nodejs

RUN node -v && npm -v

WORKDIR /usr/src/app

COPY . .

RUN npm install

RUN npm run build

RUN npm install -g serve

RUN serve -s -l 5000 build

