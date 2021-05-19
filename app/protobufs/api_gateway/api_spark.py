
import os
import grpc
from utils_pb2 import *
from spark_connector_pb2 import *
from spark_connector_pb2_grpc import Spark_ConnectorStub

spark_host = os.getenv("SPARK_CONNECTOR_HOST", "localhost")
spark_channel = grpc.insecure_channel(f"{spark_host}:50054")
spark_client = Spark_ConnectorStub(spark_channel)

def workerWithMoreConnections():
    result = spark_client.GetPersonWhoWorkedWithMorePeopleToSameMovie(Empty()).output
    result = [ line for line in result.split('\n') ]

    index = -1
    str = "+---------+----------------+"
    try :   index = len(result) - result[-1::-1].index(str) - 2
    except: pass
    if index < 0: return None

    result = [ i.replace('|','').strip()  for i in result[index].split('|') ]
    id, rating = [ i for i in result if i != ""]
    return {
        'link': "https://www.imdb.com/name/"+id,
        'rating': round(float(rating),2)
    }

def bestDirector():
    result = spark_client.GetBestDirector(Empty()).output
    result = [ line for line in result.split('\n')       \
                        if line.startswith("https://") ] \
           + [None]
    return result[0]