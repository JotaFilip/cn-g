from pyspark.sql import SparkSession
import os

import zipfile
with zipfile.ZipFile("account.zip", 'r') as zip_ref:
    zip_ref.extractall(".")
print(os.listdir())
d = os.getcwd()
spark = SparkSession \
    .builder \
    .appName("PySpark example") \
    .getOrCreate()
df = spark.read.format("jdbc").options(
    url="jdbc:mysql://34.90.227.81:3306/account",
    driver = "com.mysql.cj.jdbc.Driver",
    dbtable = "user",
    user="cngroupfcul",
    verifyServerCertificate="false",
    useSSL="true",
    requireSSL="true",
    password="178267316238hsugdhgaabhdsauisduiasiud89812989021709120783bjjkhaklnskdj").load()
df.printSchema()
print("== Row count: ", df.count(), " ==")
df.show()
spark.stop()
