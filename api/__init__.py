from flask import Blueprint
from .weather_station_routes import weather_station_routes
from .weather_data_routes import weather_data_routes

api_bp = Blueprint('api', __name__)

api_bp.register_blueprint(weather_station_routes, url_prefix='/weather-station')
api_bp.register_blueprint(weather_data_routes, url_prefix='/weather-data')