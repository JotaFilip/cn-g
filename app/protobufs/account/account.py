from models import Base, User, Seen, Like, Contagem
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
#
engine = create_engine('sqlite:///usersWithTokens.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

import sys
import secrets
from concurrent import futures

import grpc
from grpc_interceptor import ExceptionToStatusInterceptor
from grpc_interceptor.exceptions import NotFound

from account_pb2 import *
import account_pb2_grpc
from utils_pb2 import *


class AccountService(account_pb2_grpc.AccountServicer):
    def VerificarPassword(self, request, context):

        user = session.query(User).filter_by(username = request.username).first()
        if not user or not user.verify_password(request.password):
            return Success(success = True)
        return Success(success = False)

    def VerificaSeEhNovoECria(self,request,context):
        if session.query(User).filter_by(username=request.username).first() or session.query(User).filter_by(
                email=request.email).first() is not None:
            # user = session.query(User).filter_by(username=username).first()
            Success(success=False)  # Já existe
        user = User(username=request.username, email=request.email, nonce=request.nonce)
        # user.hash_password(password)
        session.add(user)
        session.commit()
        Success(success=True)

    def UserPassword(self, request, context):

        username = request.username
        password = request.password
        nonce = request.nonce
        user = session.query(User).filter_by(username=username).first()
        if user is None:
            Success(success = False)
        if not user.verify_nonce(nonce):
            Success(success = False)

        salt = secrets.randbelow(sys.maxsize)
        user.hash_password(password, str(salt))
        session.commit()

        return Success(success = True)
    def LoginUser(self, request, context):
        return None

    def LogoutUser(self, request, context):
        return None
    #

    def Seen(self,request,context):
        #user = session.query().filter_by(username=request.username).first()
        seen = Seen(user=request.user_id, item_id=request.id, item_type=request.type)
        session.add(seen)

        for cat in request.categories:
            count = session.query(Contagem).filter_by(user_id=request.user_id, category=cat)
            if count is None:
                count = Contagem(user_id = request.user_id, category = cat, likes = 0, views = 1)
                session.add(count)
            else:
                count.incrementSeens()

        session.commit()
        pass
    def Like(self,request,context):
        like = Like(user=request.user_id, item_id=request.id, item_type=request.type)
        session.add(like)
        for cat in request.categories:
            count = session.query(Contagem).filter_by(user_id=request.user_id, category=cat)
            if count is None:
                count = Contagem(user_id = request.user_id, category = cat, likes = 1, views = 0)
                session.add(count)
            else:
                count.incrementLikes()
        session.commit()
    def GetLikes(self,request,context):
        likes = session.query(Like).filter_by(user_id=request.id)
        ret = []
        for like in likes:
            ret.append(SeenAndLikeInfoReturn(id = like.item_id, type=like.type))
        return SeensAndLikesInfo(infos=ret)



    def GetSeens(self,request,context):
        seens = session.query(Seen).filter_by(user_id=request.id)
        ret = []
        for seen in seens:
            ret.append(SeenAndLikeInfoReturn(id=seen.item_id, type=seen.type))
        return SeensAndLikesInfo(infos=ret)
    def GetContagemLikesAndViews(self,request,context):
        counts = session.query(Contagem).filter_by(user_id=request.user_id)
        ret = []
        for count in counts:
            ret.append(TupleForCategory(category = count.category, views = count.views, likes = count.likes))
        return ViewsAndLikesCount(tuples = ret)



    #Username
    def GetUserByName(self, request, context):
        return None

    def UpdateUser(self, request, context):
        return None

    def DeleteUser(self, request, context):
        return None

#def GetUser(self, username):
#    # TODO
#    # results = list(db.find({ "username": username}).limit(1))
#    results = []

#    if len(results) <= 0:
#        raise NotFound("Id not found")
#    return all_lists_to_proto(results[0])

#def all_lists_to_proto(user):
 #   return LikesAndViewsResponse(
 #       books = list_to_proto(user,"books"),
  #      imdbs = list_to_proto(user,"imdbs"),
  #      animes = list_to_proto(user,"animes")
  #  )

def list_to_proto(user,type):
    return LikesAndViewsRequest(
        likes = user[type+"_likes"],
        views = user[type+"_views"],
    )

def serve():
    interceptors = [ExceptionToStatusInterceptor()]
    server = grpc.server(
        futures.ThreadPoolExecutor(max_workers=10), interceptors=interceptors
    )
    account_pb2_grpc.add_AccountServicer_to_server(
        AccountService(), server
    )
    
    server.add_insecure_port("[::]:50055")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()