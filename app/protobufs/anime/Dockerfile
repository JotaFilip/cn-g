FROM python

RUN mkdir /service
COPY app/protobufs/anime/  /service/

WORKDIR /service

RUN pip install -r requirements.txt

EXPOSE 50053
ENTRYPOINT [ "python", "anime.py" ]
