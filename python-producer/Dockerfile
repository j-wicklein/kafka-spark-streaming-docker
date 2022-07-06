FROM python:3

ADD producer.py /

WORKDIR /usr/src/app

RUN pip install kafka-python

COPY requirement.txt requirement.txt

RUN pip install -r requirement.txt

COPY twitter_data.py ./

COPY . .

CMD [ "python", "./producer.py" ]
