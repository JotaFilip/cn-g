# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import account_pb2 as account__pb2
import utils_pb2 as utils__pb2


class AccountStub(object):
    """//////////////////////////////////////////
    //////////////////////////////////////////
    //////////////////////////////////////////

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Seen = channel.unary_unary(
                '/Account/Seen',
                request_serializer=account__pb2.SeenAndLikeInfo.SerializeToString,
                response_deserializer=utils__pb2.Success.FromString,
                )
        self.Remove_Seen = channel.unary_unary(
                '/Account/Remove_Seen',
                request_serializer=account__pb2.SeenAndLikeInfo.SerializeToString,
                response_deserializer=utils__pb2.Success.FromString,
                )
        self.Like = channel.unary_unary(
                '/Account/Like',
                request_serializer=account__pb2.SeenAndLikeInfo.SerializeToString,
                response_deserializer=utils__pb2.Success.FromString,
                )
        self.Remove_Like = channel.unary_unary(
                '/Account/Remove_Like',
                request_serializer=account__pb2.SeenAndLikeInfo.SerializeToString,
                response_deserializer=utils__pb2.Success.FromString,
                )
        self.GetContagemLikesAndViews = channel.unary_unary(
                '/Account/GetContagemLikesAndViews',
                request_serializer=account__pb2.UserId.SerializeToString,
                response_deserializer=account__pb2.ViewsAndLikesCount.FromString,
                )
        self.GetUserByName = channel.unary_unary(
                '/Account/GetUserByName',
                request_serializer=account__pb2.UsernameRequest.SerializeToString,
                response_deserializer=account__pb2.UserData.FromString,
                )
        self.UpdateUser = channel.unary_unary(
                '/Account/UpdateUser',
                request_serializer=account__pb2.UpdateUserRequest.SerializeToString,
                response_deserializer=utils__pb2.Success.FromString,
                )
        self.DeleteUser = channel.unary_unary(
                '/Account/DeleteUser',
                request_serializer=account__pb2.UserRequest.SerializeToString,
                response_deserializer=utils__pb2.Success.FromString,
                )
        self.GetLikesItem = channel.unary_unary(
                '/Account/GetLikesItem',
                request_serializer=account__pb2.SeenAndLikeItem.SerializeToString,
                response_deserializer=account__pb2.CountInfo.FromString,
                )
        self.GetSeensItem = channel.unary_unary(
                '/Account/GetSeensItem',
                request_serializer=account__pb2.SeenAndLikeItem.SerializeToString,
                response_deserializer=account__pb2.CountInfo.FromString,
                )
        self.GetTopTen = channel.unary_unary(
                '/Account/GetTopTen',
                request_serializer=account__pb2.TopTenRequest.SerializeToString,
                response_deserializer=account__pb2.SeensAndLikesInfo.FromString,
                )


class AccountServicer(object):
    """//////////////////////////////////////////
    //////////////////////////////////////////
    //////////////////////////////////////////

    """

    def Seen(self, request, context):
        """Parte da library
        Marcar item como visto
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Remove_Seen(self, request, context):
        """Remover visto do item
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Like(self, request, context):
        """Marcar item como gostado
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Remove_Like(self, request, context):
        """Remover like do item
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetContagemLikesAndViews(self, request, context):
        """Obter likes do utilizador
        rpc GetLikes(UserId) returns (SeensAndLikesInfo);
        //Obter Visualizações do utilizador
        rpc GetSeens(UserId) returns (SeensAndLikesInfo);
        Obter contagem de likes e views por categoria deste utilizador
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetUserByName(self, request, context):
        """Username
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteUser(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLikesItem(self, request, context):
        """ObterContagem de likes do item
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSeensItem(self, request, context):
        """ObterContagem de seens do item
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTopTen(self, request, context):
        """Get Top Ten Animes, Books or Movies
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AccountServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Seen': grpc.unary_unary_rpc_method_handler(
                    servicer.Seen,
                    request_deserializer=account__pb2.SeenAndLikeInfo.FromString,
                    response_serializer=utils__pb2.Success.SerializeToString,
            ),
            'Remove_Seen': grpc.unary_unary_rpc_method_handler(
                    servicer.Remove_Seen,
                    request_deserializer=account__pb2.SeenAndLikeInfo.FromString,
                    response_serializer=utils__pb2.Success.SerializeToString,
            ),
            'Like': grpc.unary_unary_rpc_method_handler(
                    servicer.Like,
                    request_deserializer=account__pb2.SeenAndLikeInfo.FromString,
                    response_serializer=utils__pb2.Success.SerializeToString,
            ),
            'Remove_Like': grpc.unary_unary_rpc_method_handler(
                    servicer.Remove_Like,
                    request_deserializer=account__pb2.SeenAndLikeInfo.FromString,
                    response_serializer=utils__pb2.Success.SerializeToString,
            ),
            'GetContagemLikesAndViews': grpc.unary_unary_rpc_method_handler(
                    servicer.GetContagemLikesAndViews,
                    request_deserializer=account__pb2.UserId.FromString,
                    response_serializer=account__pb2.ViewsAndLikesCount.SerializeToString,
            ),
            'GetUserByName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetUserByName,
                    request_deserializer=account__pb2.UsernameRequest.FromString,
                    response_serializer=account__pb2.UserData.SerializeToString,
            ),
            'UpdateUser': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateUser,
                    request_deserializer=account__pb2.UpdateUserRequest.FromString,
                    response_serializer=utils__pb2.Success.SerializeToString,
            ),
            'DeleteUser': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteUser,
                    request_deserializer=account__pb2.UserRequest.FromString,
                    response_serializer=utils__pb2.Success.SerializeToString,
            ),
            'GetLikesItem': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLikesItem,
                    request_deserializer=account__pb2.SeenAndLikeItem.FromString,
                    response_serializer=account__pb2.CountInfo.SerializeToString,
            ),
            'GetSeensItem': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSeensItem,
                    request_deserializer=account__pb2.SeenAndLikeItem.FromString,
                    response_serializer=account__pb2.CountInfo.SerializeToString,
            ),
            'GetTopTen': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTopTen,
                    request_deserializer=account__pb2.TopTenRequest.FromString,
                    response_serializer=account__pb2.SeensAndLikesInfo.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Account', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Account(object):
    """//////////////////////////////////////////
    //////////////////////////////////////////
    //////////////////////////////////////////

    """

    @staticmethod
    def Seen(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Account/Seen',
            account__pb2.SeenAndLikeInfo.SerializeToString,
            utils__pb2.Success.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Remove_Seen(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Account/Remove_Seen',
            account__pb2.SeenAndLikeInfo.SerializeToString,
            utils__pb2.Success.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Like(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Account/Like',
            account__pb2.SeenAndLikeInfo.SerializeToString,
            utils__pb2.Success.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Remove_Like(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Account/Remove_Like',
            account__pb2.SeenAndLikeInfo.SerializeToString,
            utils__pb2.Success.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetContagemLikesAndViews(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Account/GetContagemLikesAndViews',
            account__pb2.UserId.SerializeToString,
            account__pb2.ViewsAndLikesCount.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetUserByName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Account/GetUserByName',
            account__pb2.UsernameRequest.SerializeToString,
            account__pb2.UserData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Account/UpdateUser',
            account__pb2.UpdateUserRequest.SerializeToString,
            utils__pb2.Success.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteUser(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Account/DeleteUser',
            account__pb2.UserRequest.SerializeToString,
            utils__pb2.Success.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLikesItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Account/GetLikesItem',
            account__pb2.SeenAndLikeItem.SerializeToString,
            account__pb2.CountInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetSeensItem(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Account/GetSeensItem',
            account__pb2.SeenAndLikeItem.SerializeToString,
            account__pb2.CountInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetTopTen(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Account/GetTopTen',
            account__pb2.TopTenRequest.SerializeToString,
            account__pb2.SeensAndLikesInfo.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
