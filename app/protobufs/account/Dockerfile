FROM python

RUN ls -la

RUN mkdir /service
COPY app/protobufs/account/  /service/

RUN ls -la service

WORKDIR /service

RUN ls -la

RUN pip install -r requirements.txt

EXPOSE 50055
ENTRYPOINT [ "python", "account.py" ]
