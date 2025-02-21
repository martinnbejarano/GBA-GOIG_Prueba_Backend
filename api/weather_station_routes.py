from flask import Blueprint, request
from models.weather_station import insert_weather_station, delete_weather_station, update_weather_station


weather_station_routes = Blueprint('weather_station_routes', __name__)

@weather_station_routes.route('', methods=['POST'])
def create_weather_station_route():
    try:
        data = request.get_json()
        name = data['name']
        latitude = float(data['latitude'])
        longitude = float(data['longitude'])

        if not (-90 <= latitude <= 90):
            return {
                "message": "Latitude must be between -90 and 90 degrees"
            }, 400
        
        if not (-180 <= longitude <= 180):
            return {
                "message": "Longitude must be between -180 and 180 degrees"
            }, 400

        station_id = insert_weather_station(name, latitude, longitude)

        return {
            "id": station_id,
            "message": f"Station {name} created",
        }, 201
    except ValueError:
        return {
            "message": "Latitude and longitude must be numbers"
        }, 400
    except KeyError:
        return {
            "message": "Name, latitude and longitude are required"
        }, 400
    except Exception as e:
        return {
            "message": str(e)
        }, 500
        
@weather_station_routes.route('/<int:station_id>', methods=['DELETE'])
def delete_weather_station_route(station_id: int):
    try:
        id_deleted = delete_weather_station(station_id)
        
        if id_deleted is None:
            return {
                "message": f"Station {station_id} not found"
            }, 404
        
        return {
            "id": station_id,
            "message": f"Station {station_id} deleted",
        }
    except Exception as e:
        return {
            "message": str(e)
        }, 500
        
@weather_station_routes.route('/<int:station_id>', methods=['PUT'])
def update_weather_station_route(station_id: int):
    try:
        data = request.get_json()

        name = data.get('name', None)
        latitude = data.get('latitude', None)
        longitude = data.get('longitude', None)
        
        if not (name or latitude or longitude):
            return {
                "message": "At least one of name, latitude or longitude must be provided"
            }, 400

        updated_station = update_weather_station(station_id, name, longitude, latitude)

        if updated_station is None:
            return {
                "message": f"Station {station_id} not found"
            }, 404

        return {
            "id": updated_station[0],  
            "name": updated_station[1], 
            "location": updated_station[2],  
            "message": f"Station {station_id} updated",
        }, 200

    except Exception as e:
        return {
            "message": str(e)
        }, 500
