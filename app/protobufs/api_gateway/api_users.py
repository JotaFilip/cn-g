
# Users API
import os

#from app.protobufs.api_gateway.api_gateway import auth0


from signin_pb2 import *

from signin_pb2_grpc import SignInStub
from account_pb2 import *
import grpc
import json
from six.moves.urllib.request import urlopen
from functools import wraps

from flask import Flask, request, jsonify, _request_ctx_stack
from flask_cors import cross_origin
from jose import jwt
import json
from six.moves.urllib.request import urlopen

from jose import jwt

AUTH0_DOMAIN = 'saldanha.eu.auth0.com'
API_AUDIENCE = 'https://recommendations.sytes.net/api'
ALGORITHMS = ["RS256"]
from grpc_interceptor import ExceptionToStatusInterceptor
#

from verifier import Verifier
from flask import Flask, jsonify, request, url_for, abort, g
#from flask_httpauth import HTTPBasicAuth

from flask import session

from flask import redirect

# with open("api_gateway.key", "rb") as fp:
    # api_gateway_key = fp.read()
# with open("api_gateway.pem", "rb") as fp:
    # api_gateway_cert = fp.read()
# with open("ca.pem", "rb") as fp:
    # ca_cert = fp.read()
# creds = grpc.ssl_channel_credentials(ca_cert, api_gateway_key, api_gateway_cert)

# auth = HTTPBasicAuth()
# sign_host = os.getenv("SIGNIN_HOST", "localhost")
# sign_channel = grpc.secure_channel(f"{sign_host}:50054", creds)
# signin_client = SignInStub(sign_channel)

#auth = HTTPBasicAuth()
sign_host = os.getenv("SIGNIN_HOST", "localhost")
sign_channel = grpc.insecure_channel(f"{sign_host}:50054", options=(('grpc.enable_http_proxy', 0),))
signin_client = SignInStub(sign_channel)


#@auth.verify_password

def verify_password(username_or_token, password, required_scopes=None):
    #Try to see if it's a token first
    user_id = Verifier.verify_auth_token(username_or_token)
    if not user_id: #significa que o token é invalido
        #user = session.query(User).filter_by(username = username_or_token).first()
        #if not user or not user.verify_password(password):
        request = VerificarRequest(username = username_or_token, password=password)
        response = signin_client.VerificarPassword(request)
        if not response.success:
            return None
        user_id = response.id

    g.user_id = user_id
    #token = g.user.generate_auth_token()
    return {'sub': user_id, 'valid': True}
    #if token:
    #    responseObject = {
    #        'status': 'success',
    #        'message': 'Successfully logged in.',
    #        'auth_token': token.decode()
    #    }
    #    return jsonify(responseObject), 200
#@auth.login_required

def verify_token(access_token) -> dict:
    jsonurl = urlopen("https://"+AUTH0_DOMAIN+"/.well-known/jwks.json")
    jwks = json.loads(jsonurl.read())
    unverified_header = jwt.get_unverified_header(access_token)
    rsa_key = {}
    for key in jwks["keys"]:
        if key["kid"] == unverified_header["kid"]:
            rsa_key = {
                "kty": key["kty"],
                "kid": key["kid"],
                "use": key["use"],
                "n": key["n"],
                "e": key["e"]
            }
    if rsa_key:
        try:
            payload = jwt.decode(
                access_token,
                rsa_key,
                algorithms=ALGORITHMS,
                audience=API_AUDIENCE,
                issuer="https://"+AUTH0_DOMAIN+"/"
            )
        except jwt.ExpiredSignatureError:
            raise AuthError({"code": "token_expired",
                             "description": "token is expired"}, 401)
        except jwt.JWTClaimsError:
            raise AuthError({"code": "invalid_claims",
                             "description":
                                 "incorrect claims,"
                                 "please check the audience and issuer"}, 401)
        except Exception:
            raise AuthError({"code": "invalid_header",
                             "description":
                                 "Unable to parse authentication"
                                 " token."}, 401)
    unverified_claims = jwt.get_unverified_claims(access_token)
    if unverified_claims.get("scope") and unverified_claims.get("sub"):
        token_scopes = unverified_claims["scope"].split()
        return {'sub': unverified_claims.get("sub"), 'scope': token_scopes}
    return None




def createUser(body):
    request =EmailRequest (
        email = body["email"],
        username = body["username"]
    )
    return signin_client.CreateUser(request).success
def givePassword(body):
    request = PasswordRequest (
        username = body["username"],
        password = body["password"],
        nonce=body["nonce"]
    )
    return signin_client.UserPassword(request).success


from six.moves.urllib.parse import urlencode

def logoutUser():
    #params = {'returnTo': url_for('home', _external=True), 'client_id': '72wQelC6FubulYS6qlY7ZhSVkyNgoTYF'}
    return redirect('https://saldanha.eu.auth0.com/v2/logout')

def getUserByName(username):
    request = UserRequest (
        username = username
    )

    resp = signin_client.GetUserByName(request)
    likes = []
    seens = []
    for r in resp.seens:
        type = "All"
        if (r.type == 0):
            type = "BOOK"
        if (r.type == 1):
            type = "SHOW"
        if (r.type == 2):
            type = "ANIME"

        object = {"id": r.id, "type": type}
        seens.append(object)
    for r in resp.likes:
        type = "All"
        if (r.type == 0):
            type = "BOOK"
        if (r.type == 1):
            type = "SHOW"
        if (r.type == 2):
            type = "ANIME"

        object = {"id": r.id, "type": type}
        likes.append(object)
    return  {"username": resp.username, "likes": likes, "seens": seens}

def updateUser(username,body):
    request = UpdateUserRequest (
        username = username,
        new_username = body["username"],
        new_password = body["password"],
    )
    return signin_client.UpdateUser(request).success

def deleteUser(username):
    request = UserRequest (
        username = username
    )
    return signin_client.DeleteUser(request).success