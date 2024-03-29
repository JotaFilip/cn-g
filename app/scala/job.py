from pyspark.sql import SparkSession
import os

spark = SparkSession \
    .builder \
    .appName("PySpark example") \
    .getOrCreate()
df = spark.read.option("header", "true").option("sep", "\t").option("inferSchema", "true").option("nullValue", "\\N").csv("gs://cn-spark-bucket/title.principals.tsv")
# df = spark.read.format("jdbc").options(
#     url="jdbc:mysql://34.90.227.81:3306/account",
#     driver = "com.mysql.cj.jdbc.Driver",
#     dbtable = "user",
#     user="cngroupfcul",
#     verifyServerCertificate="false",
#     useSSL="true",
#     requireSSL="true",
#     password="178267316238hsugdhgaabhdsauisduiasiud89812989021709120783bjjkhaklnskdj").load()
logs_df = df.select("tconst", "nconst").registerTempTable("movie_people")
edges = spark.sql("SELECT DISTINCT t1.nconst as src, t2.nconst as dst FROM movie_people t1, movie_people t2 WHERE t1.tconst == t2.tconst AND t1.nconst != t2.nconst")
verts = spark.sql("SELECT t1.nconst as id FROM movie_people t1")
edges.write.option("header","true").csv("gs://cn-spark-bucket/edges.csv")
verts.write.option("header","true").csv("gs://cn-spark-bucket/verts.csv")
# edges.printSchema()
# print("== Row count: ", edges.count(), " ==")
# edges.show()
# verts.printSchema()
# print("== Row count: ", verts.count(), " ==")
# verts.show()
#
#
# # Create a GraphFrame
# g = GraphFrame(verts, edges)
#
# # Query: Get in-degree of each vertex.
# g.inDegrees.show()

spark.stop()
