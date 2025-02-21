from flask import Flask, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
from api import api_bp
from flask_swagger_ui import get_swaggerui_blueprint

SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={  
        'app_name': "Prueba Backend"
    }
)

load_dotenv()

app = Flask(__name__)
CORS(app)

app.static_folder = 'static'

app.register_blueprint(api_bp, url_prefix='/api')
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


@app.route('/')
def index():
    return "Hello World"

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)  

if __name__ == '__main__':
    app.run(port=8000)