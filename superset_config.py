import os

MAPBOX_API_KEY = os.getenv('MAPBOX_API_KEY', '')
SQLALCHEMY_DATABASE_URI = os.getenv('SUPERSET_META_DB_URI', 'sqlite:////var/lib/superset/superset.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = os.getenv('SUPERSET_SECRET_KEY','thisISaSECRET_1234')
