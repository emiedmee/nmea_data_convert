import os

DB_USER     = os.environ.get('DB_USER') if 'DB_USER' in os.environ else 'postgres'
DB_PASSWORD = os.environ.get('DB_PASSWORD') if 'DB_PASSWORD' in os.environ else 'postgres'
DB_HOST     = os.environ.get('DB_HOST') if 'DB_HOST' in os.environ else 'localhost'
DB_PORT     = os.environ.get('DB_PORT') if 'DB_PORT' in os.environ else '5432'
DB_NAME     = os.environ.get('DB_NAME') if 'DB_NAME' in os.environ else 'nmea_data'
