from pyspark.sql import SparkSession
import os

spark = SparkSession \
    .builder \
    .appName("PySpark example") \
    .getOrCreate()
rat = spark.read.option("header", "true").option("sep", "\t").option("inferSchema", "true").option("nullValue", "\\N").csv("gs://cn-spark-bucket/title.ratings.tsv")
act = spark.read.option("header", "true").option("sep", "\t").option("inferSchema", "true").option("nullValue", "\\N").csv("gs://cn-spark-bucket/title.principals.tsv")
# df = spark.read.format("jdbc").options(
#     url="jdbc:mysql://34.90.227.81:3306/account",
#     driver = "com.mysql.cj.jdbc.Driver",
#     dbtable = "user",
#     user="cngroupfcul",
#     verifyServerCertificate="false",
#     useSSL="true",
#     requireSSL="true",
#     password="178267316238hsugdhgaabhdsauisduiasiud89812989021709120783bjjkhaklnskdj").load()
act.registerTempTable("movie_people")
rat.registerTempTable("movie_ranking")
res = spark.sql("SELECT  p.nconst, AVG(r.averageRating) as rank FROM movie_ranking r, movie_people p WHERE r.numVotes > 10000 AND p.category LIKE 'director' AND p.tconst == r.tconst GROUP BY p.nconst HAVING COUNT(r.averageRating) > 10 ORDER BY rank DESC LIMIT 1")
#verts = spark.sql("SELECT t1.nconst as id FROM movie_people t1")
# edges.printSchema()
# print("== Row count: ", edges.count(), " ==")
# edges.show()
res.printSchema()
print("== Row count: ", res.count(), " ==")
res.show()
#
#
# # Create a GraphFrame
# g = GraphFrame(verts, edges)
#
# # Query: Get in-degree of each vertex.
# g.inDegrees.show()

spark.stop()
