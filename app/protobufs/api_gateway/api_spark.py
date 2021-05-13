
import os
import grpc
from spark_connector_pb2 import *
from spark_connector_pb2_grpc import Spark_ConnectorStub

spark_host = os.getenv("SPARK_CONNECTOR_HOST", "localhost")
spark_channel = grpc.insecure_channel(f"{spark_host}:50058")
spark_client = Spark_ConnectorStub(spark_channel)

def director(name):
    # TODO
    pass

def actor():
    # TODO
    pass