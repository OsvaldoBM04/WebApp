from flask import Flask # Importar la clase Flask del módulo flask para crear la aplicación web.
from flask_sqlalchemy import SQLAlchemy # Importar la clase SQLAlchemy del módulo flask_sqlalchemy para manejar la base de datos de la aplicación.
from flask_migrate import Migrate # Importar la clase Migrate del módulo flask_migrate para manejar las migraciones de la base de datos de la aplicación.
from dotenv import load_dotenv # Importar la función load_dotenv del módulo python-dotenv para cargar variables de entorno desde un archivo .env.
from config import Config # Importar la clase Config del archivo config.py que contiene las configuraciones de la aplicación.
import logging


load_dotenv() #Carga variables de archivo .env

#Inicializar extenciones
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    #Crear la aplicación de Flask
    app = Flask(__name__,template_folder='templates',static_folder='static')
    print(app.jinja_loader.searchpath)
    #Configurar la aplicación
    app.config.from_object('config.Config') #Asignar las configutaciones que estan en la clase Config de config.py
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Osvald0.@localhost/productividad_data' # Asignar la URL de la base de datos desde el archivo .env
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Desactivar el seguimiento de modificaciones de SQLAlchemy para mejorar el rendimiento de la aplicación
    db.init_app(app) # Inicializar la base de datos con la aplicación de Flask
    migrate.init_app(app, db) # Inicializar la migración de la base de datos con la aplicación de Flask y la base de datos
    from app.routes import bp # Importar el objeto bp del archivo routes.py que contiene las rutas de
    app.register_blueprint(bp, url_prefix='/') # Registrar las rutas definidas en el archivo routes.py con la aplicación de Flask

    return app # Devolver la aplicación de Flask configurada
