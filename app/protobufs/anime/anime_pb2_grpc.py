# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import anime_pb2 as anime__pb2


class AnimeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SearchById = channel.unary_unary(
                '/Anime/SearchById',
                request_serializer=anime__pb2.AnimeByIdRequest.SerializeToString,
                response_deserializer=anime__pb2.AnimeResponse.FromString,
                )
        self.SearchByName = channel.unary_unary(
                '/Anime/SearchByName',
                request_serializer=anime__pb2.AnimeByNameRequest.SerializeToString,
                response_deserializer=anime__pb2.AnimeDataList.FromString,
                )
        self.SearchByCategory = channel.unary_unary(
                '/Anime/SearchByCategory',
                request_serializer=anime__pb2.AnimeByCategoryRequest.SerializeToString,
                response_deserializer=anime__pb2.AnimeDataList.FromString,
                )


class AnimeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SearchById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchByName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchByCategory(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AnimeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SearchById': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchById,
                    request_deserializer=anime__pb2.AnimeByIdRequest.FromString,
                    response_serializer=anime__pb2.AnimeResponse.SerializeToString,
            ),
            'SearchByName': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchByName,
                    request_deserializer=anime__pb2.AnimeByNameRequest.FromString,
                    response_serializer=anime__pb2.AnimeDataList.SerializeToString,
            ),
            'SearchByCategory': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchByCategory,
                    request_deserializer=anime__pb2.AnimeByCategoryRequest.FromString,
                    response_serializer=anime__pb2.AnimeDataList.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Anime', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Anime(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SearchById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Anime/SearchById',
            anime__pb2.AnimeByIdRequest.SerializeToString,
            anime__pb2.AnimeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchByName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Anime/SearchByName',
            anime__pb2.AnimeByNameRequest.SerializeToString,
            anime__pb2.AnimeDataList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchByCategory(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Anime/SearchByCategory',
            anime__pb2.AnimeByCategoryRequest.SerializeToString,
            anime__pb2.AnimeDataList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)