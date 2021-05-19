
# Users API
import os

#from app.protobufs.api_gateway.api_gateway import auth0


# from signin_pb2 import *
# from signin_pb2_grpc import SignInStub

import grpc

import json
from six.moves.urllib.request import urlopen

from jose import jwt

AUTH0_DOMAIN = 'saldanha.eu.auth0.com'
API_AUDIENCE = 'https://recommendations.sytes.net/api'
ALGORITHMS = ["RS256"]
from grpc_interceptor import ExceptionToStatusInterceptor
#


from flask import Flask, jsonify, request, url_for, abort, g
#from flask_httpauth import HTTPBasicAuth



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

# #auth = HTTPBasicAuth()
# sign_host = os.getenv("SIGNIN_HOST", "localhost")
# sign_channel = grpc.insecure_channel(f"{sign_host}:50054", options=(('grpc.enable_http_proxy', 0),))
# signin_client = SignInStub(sign_channel)


from account_pb2_grpc import AccountStub
from account_pb2 import *
account_host = os.getenv("ACCOUNTS_HOST", "localhost")
account_channel = grpc.insecure_channel(f"{account_host}:50055")
account_client = AccountStub(account_channel)
jsonurl = urlopen("https://"+AUTH0_DOMAIN+"/.well-known/jwks.json")
jwks = json.loads(jsonurl.read())

class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response
#@auth.verify_password

# def verify_password(username_or_token, password, required_scopes=None):
#     #Try to see if it's a token first
#     user_id = Verifier.verify_auth_token(username_or_token)
#     if not user_id: #significa que o token é invalido
#         #user = session.query(User).filter_by(username = username_or_token).first()
#         #if not user or not user.verify_password(password):
#         request = VerificarRequest(username = username_or_token, password=password)
#         response = signin_client.VerificarPassword(request)
#         if not response.success:
#             return None
#         user_id = response.id
#
#     g.user_id = user_id
#     #token = g.user.generate_auth_token()
#     return {'sub': user_id, 'valid': True}
    #if token:
    #    responseObject = {
    #        'status': 'success',
    #        'message': 'Successfully logged in.',
    #        'auth_token': token.decode()
    #    }
    #    return jsonify(responseObject), 200
#@auth.login_required

def verify_token(access_token) -> dict:

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
            handle_auth_error(AuthError({"code": "token_expired",
                             "description": "token is expired"}, 401))
        except jwt.JWTClaimsError:
            handle_auth_error(AuthError({"code": "invalid_claims",
                             "description":
                                 "incorrect claims,"
                                 "please check the audience and issuer"}, 401))
        except Exception:
            handle_auth_error(AuthError({"code": "invalid_header",
                             "description":
                                 "Unable to parse authentication"
                                 " token."}, 401))
    unverified_claims = jwt.get_unverified_claims(access_token)
    if unverified_claims.get("scope") and unverified_claims.get("sub"):
        token_scopes = unverified_claims["scope"].split()
        return {'sub': unverified_claims.get("sub"), 'scope': token_scopes}
    handle_auth_error(AuthError({"code": "invalid_header",
                                 "description":
                                     "Unable to parse authentication"
                                     " token."}, 401))

# def createUser(body):
#     request =EmailRequest (
#         email = body["email"],
#         username = body["username"]
#     )
#     return signin_client.CreateUser(request).success
# def createUsername(body):
#     request = UsernameRequest(
#         user_id = user,
#         username = body["username"]
#     )
#     return signin_client.Username(request).success


from six.moves.urllib.parse import urlencode

def logoutUser():
    return redirect('https://saldanha.eu.auth0.com/v2/logout')
def loginUser():

    #return redirect('https://saldanha.eu.auth0.com/authorize?audience=https://recommendations.sytes.net/api&response_type=token&client_id=72wQelC6FubulYS6qlY7ZhSVkyNgoTYF&redirect_uri=http%3A%2F%2Flocalhost%3A8443%2Fui%2Foauth2-redirect.html&scope=openid%20name%20email%20nickname%20read%3Asuggest%20write%3Aitem%20delete%3Aitem%20write%3Aseen%20write%3Alike%20write%3Ausername%20delete%3Ausername&state=U3VuIE1heSAwOSAyMDIxIDE0OjAwOjQ3IEdNVCswMTAwIChIb3JhIGRlIHZlcsOjbyBCcml0w6JuaWNhKQ%3D%3D')
    return redirect('https://saldanha.eu.auth0.com/authorize?audience=https://recommendations.sytes.net/api&response_type=token&client_id=72wQelC6FubulYS6qlY7ZhSVkyNgoTYF&redirect_uri=https%3A%2F%2Frecommendations.sytes.net%3A443%2Fui%2Foauth2-redirect.html&scope=openid%20name%20email%20nickname%20read%3Asuggest%20write%3Aitem%20delete%3Aitem%20write%3Aseen%20write%3Alike%20write%3Ausername%20delete%3Ausername&state=U3VuIE1heSAwOSAyMDIxIDE0OjAwOjQ3IEdNVCswMTAwIChIb3JhIGRlIHZlcsOjbyBCcml0w6JuaWNhKQ%3D%3D')

def getUserByName(username):
    request = UsernameRequest (
        username = username
    )

    resp = account_client.GetUserByName(request)
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

def updateUser(user, body):
    request = UpdateUserRequest (

        user_id = user,
        new_username = body["username"],
    )
    return account_client.UpdateUser(request).success

def deleteUser(user):
    request = UserRequest (
        user_id = user,
    )
    return account_client.DeleteUser(request).success