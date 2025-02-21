# GBA-GOIG_Prueba_Backend

API RESTful con Python Flask y PostgreSQL con PostGIS

## Prerequisitos

- Python 3.8
- PostgreSQL con PostGis
- pip (Python package installer)

## Instalación

1. Clonar el repositorio

```bash
git clone https://github.com/martinnbejarano/GBA-GOIG_Prueba_Backend.git
cd GBA-GOIG_Prueba_Backend
```

2. Crear virtual environment

````bash
python -m venv venv
source venv/bin/activate  # en Windows usar: venv\Scripts\activate```

3. Instalar dependencias
```bash
pip install -r requirements.txt
````

4. Configurar PostgreSQL con PostGIS

- Crear una base de datos en local
- Habilitar la extensión PostGIS en la base de datos:

```sql
CREATE EXTENSION postgis;
```

5. Configurar variables de entorno

Crear un archivo `.env` en la raíz del proyecto con las credenciales de tu base de datos:

```bash
DB_NAME=your_database_name
DB_HOST=localhost
DB_USER=your_postgres_user
DB_PASSWORD=your_postgres_password
DB_PORT=5432
```

6. Crear e inicializar las tablas

Ejecutar los siguientes comandos SQL en tu base de datos:

```sql
CREATE TABLE weather_stations (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    location GEOMETRY(POINT, 4326) NOT NULL
);

CREATE TABLE weather_data (
    id SERIAL PRIMARY KEY,
    station_id INTEGER REFERENCES weather_stations(id) ON DELETE CASCADE,
    temperature FLOAT NOT NULL,
    humidity FLOAT NOT NULL,
    pressure FLOAT NOT NULL,
    timestamp TIMESTAMP NOT NULL
);

INSERT INTO weather_stations (name, location)
VALUES
    ('Estación 1', ST_SetSRID(ST_MakePoint(-99.145966, 19.432608), 4326)),
    ('Estación 2', ST_SetSRID(ST_MakePoint(-98.224889, 19.033040), 4326)),
    ('Estación 3', ST_SetSRID(ST_MakePoint(-99.139238, 19.427053), 4326));

INSERT INTO weather_data (station_id, temperature, humidity, pressure, timestamp)
VALUES
    (1, 24.5, 0.6, 1013.4, '2023-03-19 10:00:00'),
    (1, 25.1, 0.7, 1012.8, '2023-03-19 11:00:00'),
    (2, 22.8, 0.5, 1015.2, '2023-03-19 10:00:00'),
    (2, 23.3, 0.6, 1015.6, '2023-03-19 11:00:00'),
    (3, 26.2, 0.8, 1011.2, '2023-03-19 10:00:00'),
    (3, 25.9, 0.7, 1011.6, '2023-03-19 11:00:00');
```

## Ejecutar la aplicacion

1. Iniciar el servidor

```bash
python main.py
```

## Documentación de la API

Acceder a la documentación Swagger UI en: `http://localhost:8000/swagger`

### Endpoints Disponibles

- **POST /api/weather-station**: Crear una nueva estación meteorológica
- **PUT /api/weather-station/{id}**: Actualizar una estación existente
- **DELETE /api/weather-station/{id}**: Eliminar una estación
- **GET /api/weather-data**: Obtener datos meteorológicos de la estación más cercana
