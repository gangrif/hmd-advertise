FROM resin/rpi-raspbian:jessie

RUN apt-get update --fix-missing
RUN apt-get install python-pip g++ python-dev


RUN pip install urllib

RUN mkdir /service

COPY ./adloop.py /service/
RUN chmod +x /service/adloop.py

CMD ["/service/adloop.py"]

