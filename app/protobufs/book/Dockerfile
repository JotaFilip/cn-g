FROM python

RUN mkdir /service
COPY app/protobufs/book/  /service/

WORKDIR /service

RUN pip install -r requirements.txt

EXPOSE 50051
ENTRYPOINT [ "python", "book.py" ]
