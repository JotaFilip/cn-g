from os import environ as env
from werkzeug.exceptions import HTTPException

from dotenv import load_dotenv, find_dotenv
from flask import Flask
from flask import jsonify
from flask import redirect
from flask import render_template
from flask import session
from flask import url_for
from authlib.integrations.flask_client import OAuth
from six.moves.urllib.parse import urlencode




# 3rd party moudles
import connexion
from flask_cors import CORS
from flask import request
from flask_cors import cross_origin
from functools import wraps
import json
from os import environ as env
from werkzeug.exceptions import HTTPException
#from settings import SWAGGER_URL, swagger_path
from yaml import Loader, load
from flask import redirect

from flask import render_template
from flask import session
from flask import url_for
from authlib.integrations.flask_client import OAuth
from six.moves.urllib.parse import urlencode
from flask_swagger_ui import get_swaggerui_blueprint
#from OpenSSL import SSL
#Create the application instance
options = {
    "swagger_ui_config" : {
        "oauth2RedirectUrl": "https://recommendations.sytes.net:443/ui/oauth2-redirect.html",



    }
}

app = connexion.App(__name__, specification_dir="./" , options = options)
#app = Flask(__name__)
SWAGGER_URL='/ui'
swagger_path= "seen.yaml"
swagger_yml = load(open(swagger_path, 'r'), Loader=Loader)
#API_URL = 'swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    swagger_path,
    config={'spec': swagger_yml,
           'oauth2RedirectUrl' : "https://recommendations.sytes.net:443/ui/oauth2-redirect.html"
    },
    # config={  # Swagger UI config overrides
    #     'app_name': "Test application"
    # },
     oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
        'clientId': "72wQelC6FubulYS6qlY7ZhSVkyNgoTYF",
    #    'clientSecret': "your-client-secret-if-required",
    #     'audience': 'https://recommendations.sytes.net/api'

    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
     }
)

app.app.register_blueprint(swaggerui_blueprint)
CORS(app.app)
app.app.config['SESSION_TYPE'] = 'memcached'
app.app.config['SECRET_KEY'] = 'super secret key'
oauth = OAuth(app.app)
auth0 = oauth.register(
    'auth0',
    client_id='72wQelC6FubulYS6qlY7ZhSVkyNgoTYF',
    client_secret='UHqFceMIWf0pzpA3CRWggxpGDxByyn_vQuw_90OdhaoascI-t5RBha4z5sRPbNJK',
    api_base_url='https://saldanha.eu.auth0.com',
    access_token_url='https://saldanha.eu.auth0.com/oauth/token',
    authorize_url='https://saldanha.eu.auth0.com/authorize',
    client_kwargs={
        #'scope': 'openid profile email',
        'scope': 'openid profile email read:suggest write:item delete:item write:seen write:like write:username delete:username',
    },
)
# app = Flask(__name__)



app.add_api("seen.yaml")



# swaggerui_blueprint = get_swaggerui_blueprint(
#     SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
#     API_URL,
#     # config={  # Swagger UI config overrides
#     #     'app_name': "Test application"
#     # },
#     # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
#     #    'clientId': "your-client-id",
#     #    'clientSecret': "your-client-secret-if-required",
#     #    'realm': "your-realms",
#     #    'appName': "your-app-name",
#     #    'scopeSeparator': " ",
#     #    'additionalQueryStringParams': {'test': "hello"}
#     # }
# )
#
#  oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
#     'clientId': "72wQelC6FubulYS6qlY7ZhSVkyNgoTYF",
# #    'clientSecret': "your-client-secret-if-required",
#     'realm': "your-realms",
#     'appName': "your-app-name",
#     'scopeSeparator': " ",
#      'scopes' : "openid"
# #    'additionalQueryStringParams': {'test': "hello"}
#  }
#
#                     )

# Call factory function to create our blueprint
#swaggerui_blueprint = get_swaggerui_blueprint(
#    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
#     API_URL,
#     config={  # Swagger UI config overrides
#         'app_name': "Test application"
#     },
    # oauth_config={  # OAuth config. See https://github.com/swagger-api/swagger-ui#oauth2-configuration .
    #    'clientId': "your-client-id",
    #    'clientSecret': "your-client-secret-if-required",
    #    'realm': "your-realms",
    #    'appName': "your-app-name",
    #    'scopeSeparator': " ",
    #    'additionalQueryStringParams': {'test': "hello"}
    # }
#)

#app.register_blueprint(swaggerui_blueprint)

# read the swagger.yml file to configure the endpoints


#context = ('api_gateway.pem', 'api_gateway.key')
#app.run(host='0.0.0.0', port=80, ssl_context=context, threaded=True, debug=True)
@app.app.route('/login')
def call():

    return auth0.authorize_redirect(redirect_uri="https://recommendations.sytes.net/callback",  audience='https://recommendations.sytes.net/api')

#app.register_blueprint(swaggerui_blueprint)
@app.app.route('/callback')
def callback_handling():

    return jsonify(auth0.authorize_access_token())
@app.app.route('/health')
def health():
    return "OK", 200












if __name__ == "__main__":

    app.run(debug=True, port=8443)


    #return auth0.authorize_redirect(redirect_uri='/callback')

    #token = Verifier.generate_auth_token(g.user_id)
    #token = g.user.generate_auth_token()
    #
    #return jsonify({'token': token.decode('ascii')})

#