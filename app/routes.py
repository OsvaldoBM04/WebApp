from flask import Blueprint, flash, render_template, request # Importar el módulo Blueprint y render_template desde el módulo flask
#from . import db # Importar el objeto db desde el módulo app
from app.utils import cargar_datos, calcular_productividad_periodo, transformar_a_mes
import pandas as pd
#import pdb

from app.models import Productividad
import pdb


bp = Blueprint('main', __name__) # Crear un objeto Blueprint llamado 'main'

@bp.route('/') # Definir una ruta para la función index
def index(): # Definir la función index
    return render_template('index.html') # Renderizar la plantilla 'index.html' y devolverla como respuesta

@bp.route('/datos', methods=['GET', 'POST'])
def datos():
    # Cargar y transformar los datos
    datos_originales = cargar_datos()  # Asegúrate de que esta función devuelva un DataFrame válido.
    datos_transformados = transformar_a_mes(datos_originales)

    # Lista de meses en español
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
             'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

    # Filtros enviados por el usuario
    municipio = request.form.get('municipio', '')
    unidad = request.form.get('unidad', '')
    año = request.form.get('año', '')

    # Filtrar datos según los valores seleccionados
    if municipio:
        datos_transformados = datos_transformados[datos_transformados['municipio'] == municipio]
    if unidad:
        datos_transformados = datos_transformados[datos_transformados['unidad'] == unidad]
    if año:
        datos_transformados = datos_transformados[datos_transformados['año'] == int(año)]

    # Preparar listas únicas para los selectores
    municipios_unicos = datos_originales['municipio'].dropna().unique().tolist()
    unidades_unicas = datos_originales['unidad'].dropna().unique().tolist()
    años_unicos = datos_transformados['año'].dropna().unique().tolist()
    periodos_unicos = ['Ninguno', 'Bimestral', 'Semestral']
    # Enviar datos a la plantilla
    return render_template(
        'datos.html',
        datos=datos_transformados.to_dict(orient='records'),
        municipios_unicos=municipios_unicos,
        unidades_unicas=unidades_unicas,
        años_unicos=años_unicos,
        periodos_unicos=periodos_unicos,
        meses=meses
    )
