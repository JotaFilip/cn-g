import sys
import secrets
from concurrent import futures

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from signin_pb2 import *
from utils_pb2 import *
import signin_pb2_grpc

from account_pb2 import AllLikesAndViewsResponse, LikesAndViewsResponse, LikesAndViewsRequest
from account_pb2_grpc import AccountStub
import os

account_host = os.getenv("ACCOUNT_HOST", "localhost")
account_channel = grpc.insecure_channel(f"{account_host}:50055")
account_client = AccountStub(account_channel)


import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "cngroupfcul@gmail.com"
password = "@GrupoComputacaomovel2021"

class SignInService(signin_pb2_grpc.SignInServicer):

    def CreateUser(self, request, context):
        email = request.email
        username = request.username
        nonce = secrets.randbelow(1000000)

        if username is None or email is None:
            Success(success=False)  # argumentos insuficientes
        response = account_client.VerificaSeEhNovoECria(request)




        s = smtplib.SMTP(smtp_server, port)
        s.starttls()
        s.login(sender_email, password)

        msg = MIMEMultipart()
        message = "Dear {}, send your (password; nonce) on the register rest_api\nnonce = {}".format(username,
                                                                                                     str(nonce))
        msg['From'] = sender_email
        msg['To'] = email
        msg['Subject'] = "Seen nonce register"

        msg.attach(MIMEText(message, 'plain'))

        s.send_message(msg)
        del msg
        return response


    def UserPassword(self, request, context):
        return account_client.UserPassword(request)

    def VerificarPassword(self, request, context):
        return account_client.VerificarPassword(request)

    def LoginUser(self, request, context):
        # convert and redirect
        return None

    def LogoutUser(self, request, context):
        # convert and redirect
        return None

    def GetUserByName(self, request, context):
        # convert and redirect
        return None

    def UpdateUser(self, request, context):
        # convert and redirect
        return None

    def DeleteUser(self, request, context):
        # convert and redirect
        return None

def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    signin_pb2_grpc.add_SignInServicer_to_server(
        SignInService(), server
    )
    
    server.add_insecure_port("[::]:50056")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
