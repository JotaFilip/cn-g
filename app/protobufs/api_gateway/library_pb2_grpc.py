# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import library_pb2 as library__pb2
import utils_pb2 as utils__pb2


class LibraryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Library = channel.unary_unary(
                '/Library/Library',
                request_serializer=library__pb2.LibPageRequest.SerializeToString,
                response_deserializer=library__pb2.ItemInfoResponse.FromString,
                )
        self.Recommend = channel.unary_unary(
                '/Library/Recommend',
                request_serializer=library__pb2.RecommendationRequest.SerializeToString,
                response_deserializer=library__pb2.ItemInfoResponse.FromString,
                )
        self.AddItem = channel.unary_unary(
                '/Library/AddItem',
                request_serializer=library__pb2.AddItemRequest.SerializeToString,
                response_deserializer=utils__pb2.Success.FromString,
                )
        self.GetItem = channel.unary_unary(
                '/Library/GetItem',
                request_serializer=library__pb2.ItemId.SerializeToString,
                response_deserializer=library__pb2.Item.FromString,
                )
        self.RemoveItem = channel.unary_unary(
                '/Library/RemoveItem',
                request_serializer=library__pb2.ItemId.SerializeToString,
                response_deserializer=utils__pb2.Success.FromString,
                )
        self.AddSeenItem = channel.unary_unary(
                '/Library/AddSeenItem',
                request_serializer=library__pb2.ItemIdAndUser.SerializeToString,
                response_deserializer=utils__pb2.Success.FromString,
                )
        self.RemoveSeenItem = channel.unary_unary(
                '/Library/RemoveSeenItem',
                request_serializer=library__pb2.ItemIdAndUser.SerializeToString,
                response_deserializer=utils__pb2.Success.FromString,
                )
        self.AddLikeItem = channel.unary_unary(
                '/Library/AddLikeItem',
                request_serializer=library__pb2.ItemIdAndUser.SerializeToString,
                response_deserializer=utils__pb2.Success.FromString,
                )
        self.RemoveLikeItem = channel.unary_unary(
                '/Library/RemoveLikeItem',
                request_serializer=library__pb2.ItemIdAndUser.SerializeToString,
                response_deserializer=utils__pb2.Success.FromString,
                )


class LibraryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Library(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Recommend(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddSeenItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveSeenItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddLikeItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveLikeItem(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LibraryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Library': grpc.unary_unary_rpc_method_handler(
                    servicer.Library,
                    request_deserializer=library__pb2.LibPageRequest.FromString,
                    response_serializer=library__pb2.ItemInfoResponse.SerializeToString,
            ),
            'Recommend': grpc.unary_unary_rpc_method_handler(
                    servicer.Recommend,
                    request_deserializer=library__pb2.RecommendationRequest.FromString,
                    response_serializer=library__pb2.ItemInfoResponse.SerializeToString,
            ),
            'AddItem': grpc.unary_unary_rpc_method_handler(
                    servicer.AddItem,
                    request_deserializer=library__pb2.AddItemRequest.FromString,
                    response_serializer=utils__pb2.Success.SerializeToString,
            ),
            'GetItem': grpc.unary_unary_rpc_method_handler(
                    servicer.GetItem,
                    request_deserializer=library__pb2.ItemId.FromString,
                    response_serializer=library__pb2.Item.SerializeToString,
            ),
            'RemoveItem': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveItem,
                    request_deserializer=library__pb2.ItemId.FromString,
                    response_serializer=utils__pb2.Success.SerializeToString,
            ),
            'AddSeenItem': grpc.unary_unary_rpc_method_handler(
                    servicer.AddSeenItem,
                    request_deserializer=library__pb2.ItemIdAndUser.FromString,
                    response_serializer=utils__pb2.Success.SerializeToString,
            ),
            'RemoveSeenItem': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveSeenItem,
                    request_deserializer=library__pb2.ItemIdAndUser.FromString,
                    response_serializer=utils__pb2.Success.SerializeToString,
            ),
            'AddLikeItem': grpc.unary_unary_rpc_method_handler(
                    servicer.AddLikeItem,
                    request_deserializer=library__pb2.ItemIdAndUser.FromString,
                    response_serializer=utils__pb2.Success.SerializeToString,
            ),
            'RemoveLikeItem': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveLikeItem,
                    request_deserializer=library__pb2.ItemIdAndUser.FromString,
                    response_serializer=utils__pb2.Success.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Library', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Library(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Library(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Library/Library',
            library__pb2.LibPageRequest.SerializeToString,
            library__pb2.ItemInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

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
            library__pb2.ItemInfoResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Library/AddItem',
            library__pb2.AddItemRequest.SerializeToString,
            utils__pb2.Success.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Library/GetItem',
            library__pb2.ItemId.SerializeToString,
            library__pb2.Item.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Library/RemoveItem',
            library__pb2.ItemId.SerializeToString,
            utils__pb2.Success.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddSeenItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Library/AddSeenItem',
            library__pb2.ItemIdAndUser.SerializeToString,
            utils__pb2.Success.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveSeenItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Library/RemoveSeenItem',
            library__pb2.ItemIdAndUser.SerializeToString,
            utils__pb2.Success.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddLikeItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Library/AddLikeItem',
            library__pb2.ItemIdAndUser.SerializeToString,
            utils__pb2.Success.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveLikeItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Library/RemoveLikeItem',
            library__pb2.ItemIdAndUser.SerializeToString,
            utils__pb2.Success.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
