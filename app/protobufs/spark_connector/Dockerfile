FROM python

RUN mkdir /service
COPY ./  /service/

WORKDIR /service

RUN pip install -r requirements.txt

EXPOSE 50058
ENTRYPOINT [ "python", "spark_connector.py" ]
