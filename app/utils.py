import os
import pandas as pd
from app.models import Productividad
from app import db  # Import the db object from your app module

def cargar_datos():
    try:
        # Consulta los datos directamente desde la base de datos MySQL
        query = Productividad.query.all()
        if not query:
            print("No se encontraron datos en la base de datos.")
            return pd.DataFrame()
        datos = pd.DataFrame([row.__dict__ for row in query])
        
        # Elimina las columnas adicionales que SQLAlchemy agrega automáticamente
        datos.drop('_sa_instance_state', axis=1, inplace=True)

# Normaliza los nombres de las columnas a minúsculas
        datos.columns = datos.columns.str.lower()
        print("Datos cargados desde MySQL con éxito.")
        print(datos.head()) # Verifica los datos cargados
        print(datos.columns)  # Verifica las columnas cargadas
        return datos
    
    except Exception as e:
        print(f"Error al cargar datos: {e}")
        return pd.DataFrame()

def calcular_productividad_periodo(datos, meses):

    # Asegurarse de que la columna 'Fecha' esté en formato datetime
    datos['Fecha'] = pd.to_datetime(datos['Fecha'], errors='coerce')
    # Ordenar por la fecha para que las agrupaciones sean cronológicas
    datos = datos.sort_values(by='Fecha')

    # Definir frecuencia de agrupación según el periodo de meses
    if meses == 2:
        freq = '2M'  # Bimestral
    elif meses == 6:
        freq = '6M'  # Semestral
    else:  # Por defecto, si no se especifica un periodo válido, no se agrupa
      # Productividad sin agrupación (ningún periodo seleccionado)
        datos['Productividad'] = datos['Consultas de unidad'] / datos['JornadasxUnidad'].round(2)  # Calcular productividad sin agrupar
        return datos    

    # Agrupar por 'Clues', 'Unidad' y periodos de la columna 'Fecha'
    datos_agrupados = datos.groupby(
        ['Clues', 'Unidad', pd.Grouper(key='Fecha', freq=freq), 'Año']
    ).agg({
        'Consultas de unidad': 'sum',
        'JornadasxUnidad': 'sum'
    }).reset_index()

     # Verifica si los datos agrupados son correctos
    print("Datos agrupados:")
    print(datos_agrupados.head())

# Cálculo de productividad
    datos_agrupados['Productividad'] = (datos_agrupados['Consultas de unidad'] / datos_agrupados['JornadasxUnidad']).round(2)  # Calcular productividad agrupada
    # Ordenar los resultados por fecha de forma descendente
    datos_agrupados = datos_agrupados.sort_values(by='Fecha', ascending=False)
    return datos_agrupados

def transformar_a_mes(datos):
    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
             'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
    try:
        columnas_necesarias = ['fecha', 'clues', 'unidad', 'año', 'jornadasxunidad', 'consultas_de_unidad', 'municipio']
        for col in columnas_necesarias:
            if col not in datos.columns:
                raise KeyError(f"La columna requerida '{col}' no existe en los datos.")

        datos['fecha'] = pd.to_datetime(datos['fecha'], errors='coerce')
        if datos['fecha'].isnull().all():
            raise ValueError("No se pudo convertir ninguna fecha válida en la columna 'fecha'.")

        datos['mes'] = datos['fecha'].dt.month
        datos['productividad'] = datos['consultas_de_unidad'] / datos['jornadasxunidad']

        # Agregar columna de período si es necesario
        datos['periodo'] = datos['mes'].apply(lambda x: (x - 1) // 2 + 1)  # Ejemplo: Bimestres

        datos_agrupados_mes = datos.pivot_table(
            index=['clues', 'unidad', 'año', 'municipio'],  # Incluye municipio en el índice
            columns='mes',
            values='productividad',
            aggfunc='sum'
        ).reset_index()

        column_mapping = {i + 1: meses[i] for i in range(12)}
        datos_agrupados_mes = datos_agrupados_mes.rename(columns=column_mapping)

        for mes in meses:
            if mes not in datos_agrupados_mes.columns:
                datos_agrupados_mes[mes] = None

        for mes in meses:
            if mes in datos_agrupados_mes.columns:
                datos_agrupados_mes[mes] = datos_agrupados_mes[mes].apply(
                    lambda x: f"{float(x):.1f}" if isinstance(x, (int, float)) else x
                )

        datos_agrupados_mes = datos_agrupados_mes.fillna("N/A")

        print("Datos agrupados por mes:")
        print(datos_agrupados_mes.head())

        return datos_agrupados_mes

    except Exception as e:
        print(f"Error en la transformación de datos a mes: {e}")
        return pd.DataFrame()


def calcular_productividad_periodo(datos, meses):
    # Asegurarse de que la columna 'fecha' esté en formato datetime
    datos['fecha'] = pd.to_datetime(datos['fecha'], errors='coerce')

    # Ordenar por la fecha para que las agrupaciones sean cronológicas
    datos = datos.sort_values(by='fecha')

    # Definir frecuencia de agrupación según el periodo de meses
    if meses == 2:
        freq = '2M'  # Bimestral
    elif meses == 6:
        freq = '6M'  # Semestral
    else:
        datos['productividad'] = datos['consultas de unidad'] / datos['jornadasxunidad']
        return datos

    # Agrupar por 'clues' y 'unidad' y calcular productividad
    datos_grouped = datos.groupby(['clues', 'unidad', pd.Grouper(key='fecha', freq=freq)]).agg({
        'consultas de unidad': 'sum',
        'jornadasxunidad': 'sum'
    }).reset_index()

    # Calcular la productividad para cada grupo
    datos_grouped['productividad'] = datos_grouped['consultas de unidad'] / datos_grouped['jornadasxunidad']
    return datos_grouped