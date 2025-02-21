from db import get_db_connection

SELECT_LAST_WEATHER_DATA = """
            select temperature, humidity, pressure, timestamp
            from weather_data
            where station_id = %s
            order by timestamp desc
            limit 1;
        """
        
def get_last_weather_data(station_id: int) -> tuple:
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute(SELECT_LAST_WEATHER_DATA, (station_id,))
            return cursor.fetchone()