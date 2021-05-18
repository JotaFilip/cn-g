FROM python

RUN mkdir /service
COPY ./  /service/

WORKDIR /service

RUN pip install -r requirements.txt
RUN pip install git+https://github.com/clips/pattern@development#egg=pattern

EXPOSE 50054
ENTRYPOINT [ "python", "spark_connector.py" ]
