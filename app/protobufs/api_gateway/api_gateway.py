# 3rd party moudles
import connexion
from flask_cors import CORS

from OpenSSL import SSL

# Create the application instance
app = connexion.App(__name__, specification_dir="./")

# read the swagger.yml file to configure the endpoints
app.add_api("seen.yaml")


#context = ('api_gateway.pem', 'api_gateway.key')
#app.run(host='0.0.0.0', port=80, ssl_context=context, threaded=True, debug=True)


app.run(port=80)
CORS(app.app)

if __name__ == "__main__":
    app.run(debug=True)