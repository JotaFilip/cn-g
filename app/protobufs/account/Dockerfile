FROM python

RUN mkdir /service
COPY app/protobufs/account/  /service/

WORKDIR /service

RUN pip install -r requirements.txt

EXPOSE 50055
ENTRYPOINT [ "python", "account.py" ]
