# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import spark_connector_pb2 as spark__connector__pb2
import utils_pb2 as utils__pb2


class Spark_ConnectorStub(object):
    """message DirectorWork {
    string name = 1;
    repeated Movie movies = 2;
    }

    message Movie {
    string name = 1;
    repeated string actors = 2;
    }

    message ActorName {
    string name = 1;
    }

    //////////////////////////////////////////
    //////////////RPC SERVICES////////////////
    //////////////////////////////////////////

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetPersonWhoWorkedWithMorePeopleToSameMovie = channel.unary_unary(
                '/Spark_Connector/GetPersonWhoWorkedWithMorePeopleToSameMovie',
                request_serializer=utils__pb2.Empty.SerializeToString,
                response_deserializer=spark__connector__pb2.ExecutionResult.FromString,
                )
        self.GetBestDirector = channel.unary_unary(
                '/Spark_Connector/GetBestDirector',
                request_serializer=utils__pb2.Empty.SerializeToString,
                response_deserializer=spark__connector__pb2.ExecutionResult.FromString,
                )


class Spark_ConnectorServicer(object):
    """message DirectorWork {
    string name = 1;
    repeated Movie movies = 2;
    }

    message Movie {
    string name = 1;
    repeated string actors = 2;
    }

    message ActorName {
    string name = 1;
    }

    //////////////////////////////////////////
    //////////////RPC SERVICES////////////////
    //////////////////////////////////////////

    """

    def GetPersonWhoWorkedWithMorePeopleToSameMovie(self, request, context):
        """DirectorWork);
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBestDirector(self, request, context):
        """ActorName);
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_Spark_ConnectorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetPersonWhoWorkedWithMorePeopleToSameMovie': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPersonWhoWorkedWithMorePeopleToSameMovie,
                    request_deserializer=utils__pb2.Empty.FromString,
                    response_serializer=spark__connector__pb2.ExecutionResult.SerializeToString,
            ),
            'GetBestDirector': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBestDirector,
                    request_deserializer=utils__pb2.Empty.FromString,
                    response_serializer=spark__connector__pb2.ExecutionResult.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Spark_Connector', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Spark_Connector(object):
    """message DirectorWork {
    string name = 1;
    repeated Movie movies = 2;
    }

    message Movie {
    string name = 1;
    repeated string actors = 2;
    }

    message ActorName {
    string name = 1;
    }

    //////////////////////////////////////////
    //////////////RPC SERVICES////////////////
    //////////////////////////////////////////

    """

    @staticmethod
    def GetPersonWhoWorkedWithMorePeopleToSameMovie(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Spark_Connector/GetPersonWhoWorkedWithMorePeopleToSameMovie',
            utils__pb2.Empty.SerializeToString,
            spark__connector__pb2.ExecutionResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBestDirector(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Spark_Connector/GetBestDirector',
            utils__pb2.Empty.SerializeToString,
            spark__connector__pb2.ExecutionResult.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
