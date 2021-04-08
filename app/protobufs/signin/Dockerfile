FROM python

RUN mkdir /service
COPY app/protobufs/signin/  /service/

WORKDIR /service

RUN pip install -r requirements.txt

EXPOSE 50056
ENTRYPOINT [ "python", "signin.py" ]
