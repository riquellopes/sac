FROM node:8-alpine
MAINTAINER Henrique Lopes

RUN mkdir /frontend
WORKDIR /frontend

ADD . /frontend/
# Installing project dependencies.
RUN npm install
RUN npm run build
