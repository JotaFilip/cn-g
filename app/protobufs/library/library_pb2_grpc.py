# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import anime_pb2 as anime__pb2
import book_pb2 as book__pb2
import imdb_pb2 as imdb__pb2
import library_pb2 as library__pb2


class LibraryStub(object):
    """//////////////////////////////////////////
    //////////////////////////////////////////
    //////////////////////////////////////////

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Recommend = channel.unary_unary(
                '/Library/Recommend',
                request_serializer=library__pb2.RecommendationRequest.SerializeToString,
                response_deserializer=library__pb2.BasicInfoResponse.FromString,
                )
        self.GetBook = channel.unary_unary(
                '/Library/GetBook',
                request_serializer=book__pb2.BookByIdRequest.SerializeToString,
                response_deserializer=book__pb2.BookData.FromString,
                )
        self.GetIMDB = channel.unary_unary(
                '/Library/GetIMDB',
                request_serializer=imdb__pb2.IMDBByIdRequest.SerializeToString,
                response_deserializer=imdb__pb2.IMDBData.FromString,
                )
        self.GetAnime = channel.unary_unary(
                '/Library/GetAnime',
                request_serializer=anime__pb2.AnimeByIdRequest.SerializeToString,
                response_deserializer=anime__pb2.AnimeData.FromString,
                )
        self.SearchByName = channel.unary_unary(
                '/Library/SearchByName',
                request_serializer=library__pb2.SearchByNameRequest.SerializeToString,
                response_deserializer=library__pb2.BasicInfoResponse.FromString,
                )
        self.SearchByCategory = channel.unary_unary(
                '/Library/SearchByCategory',
                request_serializer=library__pb2.SearchByCategoryRequest.SerializeToString,
                response_deserializer=library__pb2.BasicInfoResponse.FromString,
                )


class LibraryServicer(object):
    """//////////////////////////////////////////
    //////////////////////////////////////////
    //////////////////////////////////////////

    """

    def Recommend(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBook(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetIMDB(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAnime(self, request, context):
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


def add_LibraryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Recommend': grpc.unary_unary_rpc_method_handler(
                    servicer.Recommend,
                    request_deserializer=library__pb2.RecommendationRequest.FromString,
                    response_serializer=library__pb2.BasicInfoResponse.SerializeToString,
            ),
            'GetBook': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBook,
                    request_deserializer=book__pb2.BookByIdRequest.FromString,
                    response_serializer=book__pb2.BookData.SerializeToString,
            ),
            'GetIMDB': grpc.unary_unary_rpc_method_handler(
                    servicer.GetIMDB,
                    request_deserializer=imdb__pb2.IMDBByIdRequest.FromString,
                    response_serializer=imdb__pb2.IMDBData.SerializeToString,
            ),
            'GetAnime': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAnime,
                    request_deserializer=anime__pb2.AnimeByIdRequest.FromString,
                    response_serializer=anime__pb2.AnimeData.SerializeToString,
            ),
            'SearchByName': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchByName,
                    request_deserializer=library__pb2.SearchByNameRequest.FromString,
                    response_serializer=library__pb2.BasicInfoResponse.SerializeToString,
            ),
            'SearchByCategory': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchByCategory,
                    request_deserializer=library__pb2.SearchByCategoryRequest.FromString,
                    response_serializer=library__pb2.BasicInfoResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Library', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Library(object):
    """//////////////////////////////////////////
    //////////////////////////////////////////
    //////////////////////////////////////////

    """

    @staticmethod
    def Recommend(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Library/Recommend',
            library__pb2.RecommendationRequest.SerializeToString,
            library__pb2.BasicInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBook(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Library/GetBook',
            book__pb2.BookByIdRequest.SerializeToString,
            book__pb2.BookData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetIMDB(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Library/GetIMDB',
            imdb__pb2.IMDBByIdRequest.SerializeToString,
            imdb__pb2.IMDBData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAnime(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Library/GetAnime',
            anime__pb2.AnimeByIdRequest.SerializeToString,
            anime__pb2.AnimeData.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/Library/SearchByName',
            library__pb2.SearchByNameRequest.SerializeToString,
            library__pb2.BasicInfoResponse.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/Library/SearchByCategory',
            library__pb2.SearchByCategoryRequest.SerializeToString,
            library__pb2.BasicInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
