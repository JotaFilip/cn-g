FROM python

RUN mkdir /service
COPY protobufs/ /service/protobufs/
COPY imdb/ /service/imdb/

WORKDIR /service/imdb

RUN pip install -r requirements.txt
# RUN python3 -m grpc_tools.protoc -I /service/protobufs --python_out=/service/protobufs/book/ --grpc_python_out=/service/protobufs/book/ /service/protobufs/book.proto

EXPOSE 50052
ENTRYPOINT [ "python", "imdb.py" ]
