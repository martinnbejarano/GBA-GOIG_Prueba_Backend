from flask import Blueprint, request
from models.weather_station import get_closest_weather_station
from models.weather_data import get_last_weather_data

weather_data_routes = Blueprint('weather_data_routes', __name__)

@weather_data_routes.route('/', methods=['GET'])
def get_weather_data():
    try:
        longitude = float(request.args.get('longitude'))
        latitude = float(request.args.get('latitude'))
        
        station = get_closest_weather_station(longitude=longitude, latitude=latitude)
        
        if station:
            station_id = station[0]
            station_name = station[1] 
            
            weather_data = get_last_weather_data(station_id)
            
            if weather_data:
                temperature, humidity, pressure, timestamp = weather_data
                
                return {
                        "station_name": station_name,
                        "temperature": temperature,
                        "humidity": humidity,
                        "pressure": pressure,
                        "timestamp": timestamp
                    }, 200

            else:
                return {
                    "message": "No weather data found for this station"
                }, 404
        else:
            return {
                "message": "No weather stations found"
            }, 404
            
    except TypeError:
        return {
            "message": "Missing required query parameters: latitude and longitude"
        }, 400
        
    except ValueError:
        return {
            "message": "Latitude and longitude must be numbers"
        }, 400
