import sqlalchemy
from sqlalchemy.exc import IntegrityError

from models import Base, User, Seen, Like, Contagem
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
#

SQLALCHEMY_DATABASE_URI = sqlalchemy.engine.url.URL.create(
    drivername="mysql+mysqlconnector",
    username="cngroupfcul",
    password="178267316238hsugdhgaabhdsauisduiasiud89812989021709120783bjjkhaklnskdj",
    host="34.90.227.81",
    port=3306,
    database="account",
    query={"ssl_ca": "server-ca.pem"},
)


#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://cngroupfcul:178267316238hsugdhgaabhdsauisduiasiud89812989021709120783bjjkhaklnskdj@saldanha.sytes.net:3306/account?ssl=true'
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://cngroupfcul:178267316238hsugdhgaabhdsauisduiasiud89812989021709120783bjjkhaklnskdj@127.0.0.1:3306/account'
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://cngroupfcul:178267316238hsugdhgaabhdsauisduiasiud89812989021709120783bjjkhaklnskdj@192.168.1.250:3306/account'

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
        engine = create_engine(SQLALCHEMY_DATABASE_URI)

        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        user = session.query(User).filter_by(username = request.username).first()
        if user is None:
            return VerificarResponse(success = False)
        id = user.getId()
        session.commit()
        if not user.verify_password(request.password):
            return VerificarResponse(success = False)
        return VerificarResponse(success = True, id = id)
    def VerificarAdmin(self, request, context):
        engine = create_engine(SQLALCHEMY_DATABASE_URI)

        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        user = session.query(User).filter_by(id = request.id).first()
        t = user.admin
        session.commit()
        return Success(success = t)

    def VerificaSeEhNovoECria(self,request,context):
        engine = create_engine(SQLALCHEMY_DATABASE_URI)

        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        a= session.query(User).filter_by(username=request.username).first()
        b= session.query(User).filter_by(
                email=request.email).first()
        if a or b is not None:
            # user = session.query(User).filter_by(username=username).first()
            if a is not None:
                a.nonce = request.nonce
            else:
                b.nonce = request.nonce
            session.commit()
            return Success(success=False)  # Já existe mas actualiza nonce
        user = User(username=request.username, email=request.email, nonce=request.nonce)
        # user.hash_password(password)
        session.add(user)
        session.commit()
        return Success(success=True)

    def UserPassword(self, request, context):
        engine = create_engine(SQLALCHEMY_DATABASE_URI)

        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()

        username = request.username
        password = request.password
        nonce = request.nonce
        user = session.query(User).filter_by(username=username).first()
        if user is None:
            session.rollback()
            return Success(success = False)
        if not user.verify_nonce(nonce):
            session.rollback()
            return Success(success = False)

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
        engine = create_engine(SQLALCHEMY_DATABASE_URI)

        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        #user = session.query().filter_by(username=request.username).first()
        #TODO verificar se já existe antes
        seen = Seen(user_id=request.user_id, item_id=request.id, item_type=request.type)
        try:
            session.add(seen)
            session.commit()
        except IntegrityError:
            session.rollback()
        for cat in request.categories:
            count = session.query(Contagem).filter_by(user_id=request.user_id, category=cat).first()
            if count is None:
                count = Contagem(user_id = request.user_id, category = cat, likes = 0, views = 1)
                session.add(count)
            else:
                count.incrementSeens()


        session.commit()
        return Success(success=True)
    def Like(self,request,context):
        engine = create_engine(SQLALCHEMY_DATABASE_URI)

        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        #TODO verificar se já existe antes
        like = Like(user_id=request.user_id, item_id=request.id, item_type=request.type)
        try:
            session.add(like)
            session.commit()
        except IntegrityError:
            session.rollback()
            return Success(success=False)

        for cat in request.categories:
            count = session.query(Contagem).filter_by(user_id=request.user_id, category=cat).first()
            if count is None:
                count = Contagem(user_id = request.user_id, category = cat, likes = 1, views = 0)
                session.add(count)
            else:
                count.incrementLikes()
        session.commit()
        return Success(success=True)
    def GetLikes(self,request,context):
        engine = create_engine(SQLALCHEMY_DATABASE_URI)

        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        likes = session.query(Like).filter_by(user_id=request.id).all()
        ret = []
        for like in likes:
            ret.append(SeenAndLikeInfoReturn(id = like.item_id, type=like.type))
        session.commit()
        return SeensAndLikesInfo(infos=ret)



    def GetSeens(self,request,context):
        engine = create_engine(SQLALCHEMY_DATABASE_URI)

        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        seens = session.query(Seen).filter_by(user_id=request.id).all()
        ret = []
        for seen in seens:
            ret.append(SeenAndLikeInfoReturn(id=seen.item_id, type=seen.type))
        session.commit()
        return SeensAndLikesInfo(infos=ret)
    def GetContagemLikesAndViews(self,request,context):
        engine = create_engine(SQLALCHEMY_DATABASE_URI)

        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        counts = session.query(Contagem).filter_by(user_id=request.id).all()
        ret = []
        for count in counts:
            ret.append(TupleForCategory(category = count.category, views = count.views, likes = count.likes))
        session.commit()
        return ViewsAndLikesCount(tuples = ret)

    def GetLikesItem(self, request, context):
        engine = create_engine(SQLALCHEMY_DATABASE_URI)

        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        counts = session.query(Like).filter_by(item_id=request.id, item_type=request.type).count()
        session.commit()
        return CountInfo(count=counts)
    def GetSeensItem(self, request, context):
        engine = create_engine(SQLALCHEMY_DATABASE_URI)

        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        counts = session.query(Seen).filter_by(item_id=request.id, item_type=request.type).count()
        session.commit()
        return CountInfo(count=counts)



    #Username
    def GetUserByName(self, request, context):
        engine = create_engine(SQLALCHEMY_DATABASE_URI)

        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        user = session.query(User).filter_by(username=request.username).first()
        if user is None:
            session.rollback()
            return UserData()
        likes = session.query(Like).filter_by(user_id=user.id).all()
        seens = session.query(Seen).filter_by(user_id=user.id).all()
        likes = [SeenAndLikeInfoReturn(id=c.item_id, type=c.item_type) for c in likes]
        seens = [SeenAndLikeInfoReturn(id=c.item_id, type=c.item_type) for c in seens]
        session.rollback()
        return UserData(username = request.username, likes = likes, seens = seens)

    def UpdateUser(self, request, context):
        engine = create_engine(SQLALCHEMY_DATABASE_URI)

        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        user = session.query(User).filter_by(username=request.username).first()
        userb = session.query(User).filter_by(username=request.new_username).first()
        if user is None or userb is not None:
            session.rollback()
            return Success(success=False)
        salt = secrets.randbelow(sys.maxsize)
        user.hash_password(request.new_password, str(salt))
        user.username = request.new_username
        session.commit()
        return Success(success=True)

    def DeleteUser(self, request, context):
        engine = create_engine(SQLALCHEMY_DATABASE_URI)

        Base.metadata.bind = engine
        DBSession = sessionmaker(bind=engine)
        session = DBSession()
        user = session.query(User).filter_by(username=request.username).first()
        if user is not None:
            session.delete(user)
        session.commit()
        return  Success(success=user is not None)

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
    
    # with open("account.key", "rb") as fp:
        # account_key = fp.read()
    # with open("account.pem", "rb") as fp:
        # account_cert = fp.read()
    # with open("ca.pem", "rb") as fp:
        # ca_cert = fp.read()

    # creds = grpc.ssl_server_credentials(
        # [(account_key, account_cert)],
        # root_certificates=ca_cert,
        # require_client_auth=True,
    # )
    
    # server.add_secure_port("[::]:50055", creds)
    server.add_insecure_port("[::]:50055")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
