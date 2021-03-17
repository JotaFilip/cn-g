FROM python

RUN mkdir /service
COPY app/protobufs/anime/  /service/
COPY app/protobufs/book/  /service/
COPY app/protobufs/imdb/  /service/
COPY app/protobufs/library/  /service/

WORKDIR /service

RUN pip install -r requirements.txt

EXPOSE 50050
ENTRYPOINT [ "python", "library.py" ]
