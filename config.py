import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave_secreta_super_segura'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+mysqlconnector://root:Osvald0.@localhost/productividad_data'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
