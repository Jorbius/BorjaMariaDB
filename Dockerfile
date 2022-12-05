FROM python:latest

WORKDIR /usr/src/app

COPY app.py .

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get install -y python3-pip
RUN pip install pymysql

CMD [ "sleep", "10" ]
CMD [ "python3", "app.py" ]
