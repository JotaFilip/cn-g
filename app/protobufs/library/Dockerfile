FROM python

RUN mkdir /service
COPY ./  /service/

WORKDIR /service

RUN pip install -r requirements.txt

EXPOSE 50050
ENTRYPOINT [ "python", "library.py" ]
