from concurrent import futures
import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound
from pymongo import MongoClient
from bson.objectid import ObjectId

from spark_connector_pb2 import *
import spark_connector_pb2_grpc

class Spark_Connector(spark_connector_pb2_grpc.Spark_ConnectorServicer):

    def GetDirectorWork(self,request,context):
        # TODO
        pass

    def GetFamousActor(self,request,context):
        # TODO
        pass

def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    spark_connector_pb2_grpc.add_BookServicer_to_server(
        Spark_Connector(), server
    )
    
    server.add_insecure_port("[::]:50058")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()