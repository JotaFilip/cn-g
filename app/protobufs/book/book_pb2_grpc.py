# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import book_pb2 as book__pb2


class BookStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetBooks = channel.unary_unary(
                '/Book/GetBooks',
                request_serializer=book__pb2.GetBooksRequest.SerializeToString,
                response_deserializer=book__pb2.BookDataList.FromString,
                )
        self.SearchById = channel.unary_unary(
                '/Book/SearchById',
                request_serializer=book__pb2.BookByIdRequest.SerializeToString,
                response_deserializer=book__pb2.BookResponse.FromString,
                )
        self.SearchByName = channel.unary_unary(
                '/Book/SearchByName',
                request_serializer=book__pb2.BooksByNameRequest.SerializeToString,
                response_deserializer=book__pb2.BookDataList.FromString,
                )
        self.SearchByCategory = channel.unary_unary(
                '/Book/SearchByCategory',
                request_serializer=book__pb2.BooksByCategoryRequest.SerializeToString,
                response_deserializer=book__pb2.BookDataList.FromString,
                )


class BookServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetBooks(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

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


def add_BookServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetBooks': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBooks,
                    request_deserializer=book__pb2.GetBooksRequest.FromString,
                    response_serializer=book__pb2.BookDataList.SerializeToString,
            ),
            'SearchById': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchById,
                    request_deserializer=book__pb2.BookByIdRequest.FromString,
                    response_serializer=book__pb2.BookResponse.SerializeToString,
            ),
            'SearchByName': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchByName,
                    request_deserializer=book__pb2.BooksByNameRequest.FromString,
                    response_serializer=book__pb2.BookDataList.SerializeToString,
            ),
            'SearchByCategory': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchByCategory,
                    request_deserializer=book__pb2.BooksByCategoryRequest.FromString,
                    response_serializer=book__pb2.BookDataList.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Book', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Book(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetBooks(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Book/GetBooks',
            book__pb2.GetBooksRequest.SerializeToString,
            book__pb2.BookDataList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
        return grpc.experimental.unary_unary(request, target, '/Book/SearchById',
            book__pb2.BookByIdRequest.SerializeToString,
            book__pb2.BookResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/Book/SearchByName',
            book__pb2.BooksByNameRequest.SerializeToString,
            book__pb2.BookDataList.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/Book/SearchByCategory',
            book__pb2.BooksByCategoryRequest.SerializeToString,
            book__pb2.BookDataList.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
