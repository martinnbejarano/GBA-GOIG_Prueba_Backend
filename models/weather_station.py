from db import get_db_connection

INSERT_WEATHER_STATION = """
 insert into weather_stations (name, location) 
 values (%s, ST_SetSRID(ST_MakePoint(%s, %s), 4326)) 
 returning id;
"""

DELETE_WEATHER_STATION = """
    delete from weather_stations
    where id = %s
    returning id;
"""

UPDATE_WEATHER_STATION = """
    update weather_stations
    set
        name = coalesce(%s, name),
        location = coalesce(ST_SetSRID(ST_MakePoint(%s, %s), 4326), location)
    where id = %s
    returning *;
"""

SELECT_CLOSEST_WEATHER_STATION = """
    select id, name, ST_Distance(location, ST_SetSRID(ST_MakePoint(%s, %s), 4326)) as distance
    from weather_stations
    order by distance asc
    limit 1;
    """

def insert_weather_station(name: str, longitude: float, latitude: float) -> int:
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(INSERT_WEATHER_STATION, (name, longitude, latitude))
            return cursor.fetchone()[0]

def delete_weather_station(station_id: int) -> int:
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(DELETE_WEATHER_STATION, (station_id,))
            result = cursor.fetchone()
            
            if result is None:
                return None
            
            return result[0]

def update_weather_station(station_id: int, name: str, longitude: float, latitude: float) -> tuple:
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(UPDATE_WEATHER_STATION, (name, longitude, latitude, station_id))
            return cursor.fetchone()
        
def get_closest_weather_station(longitude: float, latitude: float) -> tuple:
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_CLOSEST_WEATHER_STATION, (longitude, latitude))
            return cursor.fetchone()