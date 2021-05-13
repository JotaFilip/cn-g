from job_fetch import ImportData

views = ImportData().import_views()
from pyspark.sql import SparkSession

spark = SparkSession \
        .builder \
        .appName("Views") \
        .getOrCreate()

spark_views = spark.sparkContext.parallelize(views)

item_id = "606e25ad5e927a606f53428b"
item_tp = 0

results = spark_views.filter(lambda x : x.item_id   == item_id and \
                                        x.item_type == item_tp)    \
                     .count()