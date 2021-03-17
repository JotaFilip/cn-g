FROM python

RUN mkdir /service
COPY protobufs/ /service/protobufs/
COPY book/ /service/book/

WORKDIR /service/book

RUN pip install -r requirements.txt
# RUN python3 -m grpc_tools.protoc -I /service/protobufs --python_out=/service/protobufs/book/ --grpc_python_out=/service/protobufs/book/ /service/protobufs/book.proto

EXPOSE 50051
ENTRYPOINT [ "python", "book.py" ]
