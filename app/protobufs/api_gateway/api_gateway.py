# 3rd party moudles
import connexion
from flask_cors import CORS

# Create the application instance
app = connexion.App(__name__, specification_dir="./")

# read the swagger.yml file to configure the endpoints
app.add_api("seen.yaml")
app.run(port=5000)
CORS(app.app)

if __name__ == "__main__":
    app.run(debug=True)