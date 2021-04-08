FROM python

RUN mkdir /service
COPY app/protobufs/account/  /service/

WORKDIR /service

RUN pip install -r requirements.txt
# RUN sudo apt update
# RUN sudo apt-get install python3-pymysql
RUN pip install PyMySQL
# RUN sudo apt install libmariadb-dev-compat libmariadb-dev
RUN pip install mariadb

EXPOSE 50055
ENTRYPOINT [ "python", "account.py" ]
