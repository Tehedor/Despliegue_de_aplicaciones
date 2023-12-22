FROM node:12.18.1-slim

WORKDIR /opt/microservices

COPY ratings/ ./

ENV SERVICE_VERSION v1

RUN npm install

EXPOSE 9080

CMD ["node", "ratings.js", "9080"]