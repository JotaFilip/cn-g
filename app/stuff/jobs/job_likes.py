from job_fetch import ImportData

likes = ImportData().import_likes()
from pyspark.sql import SparkSession

spark = SparkSession \
        .builder \
        .appName("Likes") \
        .getOrCreate()

spark_likes = spark.sparkContext.parallelize(likes)

item_id = ""
item_tp = ""

results = spark_likes.filter(lambda x : x.item_id == item_id and \
                                        x.item_type == item_tp)  \
                     .count()