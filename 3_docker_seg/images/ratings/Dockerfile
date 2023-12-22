FROM node:12.18.1-slim
# FROM node:18.6.0-slim

WORKDIR /opt/microservices

# COPY /product-page/practica_creativa2/bookinfo/src/ratings/package.json .
# COPY /product-page/practica_creativa2/bookinfo/src/ratings/ratings.js .
# COPY ratings/package.json /opt/microservices/ratings/package.json
# COPY ratings/ratings.js /opt/microservices/ratings/ratings.js 
COPY ratings/ ./
# COPY ratings/ /opt/microservices/
# COPY ratings/ratings.js /opt/microservices/ratings/ratings.js 

ENV SERVICE_VERSION v1

RUN npm install

EXPOSE 9080

# CMD node ratings.js 9080
CMD ["node", "ratings.js", "9080"]