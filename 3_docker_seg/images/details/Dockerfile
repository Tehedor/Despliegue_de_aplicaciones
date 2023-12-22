FROM ruby:2.7.1-slim
# FROM ruby:3.1.2-slim

WORKDIR /opt/microservices

# COPY details/details.rb /opt/microservices/details.rb
COPY details/details.rb ./
# COPY /product-page/practica_creativa2/bookinfo/src/details/details.rb .

ENV SERVICE_VERSION v1
ENV ENABLE_EXTERNAL_BOOK_SERVICE true

EXPOSE 9080

# CMD ruby details.rb 9080
CMD ["ruby","details.rb","9080"]