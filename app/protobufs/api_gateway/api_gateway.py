# 3rd party moudles
import connexion
from flask_cors import CORS
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
from OpenSSL import SSL
#Create the application instance
# options = {
#     "swagger_ui_config" : {
#         "oauth2RedirectUrl": "recommendations.sytes.net:8443/lib",
#
#
#
#     }
# }
# , options = options
app = connexion.App(__name__, specification_dir="./")
#app = Flask(__name__)
SWAGGER_URL='/ui/'
swagger_path= "seen.yaml"
swagger_yml = load(open(swagger_path, 'r'), Loader=Loader)
#API_URL = 'swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
    swagger_path,
    config={'spec': swagger_yml,
 #           'oauth2RedirectUrl' : "http://localhost:8443/callback"},
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










if __name__ == "__main__":

    app.run(debug=True, port=8443)


    #return auth0.authorize_redirect(redirect_uri='/callback')

    #token = Verifier.generate_auth_token(g.user_id)
    #token = g.user.generate_auth_token()
    #
    #return jsonify({'token': token.decode('ascii')})

#