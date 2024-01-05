FROM python:3.9.18

WORKDIR /app

COPY productpage ./

RUN pip3 install -r requirements.txt

EXPOSE 9080

CMD ["python3","productpage_monolith.py", "9080"]