
import os
import grpc
from utils_pb2 import *
from spark_connector_pb2 import *
from spark_connector_pb2_grpc import Spark_ConnectorStub

spark_host = os.getenv("SPARK_CONNECTOR_HOST", "localhost")
spark_channel = grpc.insecure_channel(f"{spark_host}:50058")
spark_client = Spark_ConnectorStub(spark_channel)

def workerWithMoreConnections():
    resp = spark_client.GetPersonWhoWorkedWithMorePeopleToSameMovie(Empty()).output
    return resp

def bestDirector():
    result = spark_client.GetBestDirector(Empty()).output
    result = [ line for line in result.split('\n')       \
                        if line.startswith("https://") ] \
           + [None]
    return result[0]