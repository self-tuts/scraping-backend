FROM python:3.4.9-alpine3.8


RUN apk add --no-cache --virtual .pynacl_deps build-base py-pip jpeg-dev libffi-dev zlib-dev openssl-dev jq

COPY requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 --no-cache-dir install -r requirements.txt


COPY . /app

ENTRYPOINT ["sh"]

CMD ["workerStart1.sh"]


