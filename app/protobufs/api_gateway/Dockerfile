FROM python

RUN mkdir /service
COPY app/protobufs/api_gateway/  /service/

WORKDIR /service

RUN pip install -r requirements.txt

EXPOSE 5000
ENTRYPOINT [ "python", "api_gateway.py" ]
