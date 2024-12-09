from . import db
class Productividad(db.Model):
    __tablename__ = 'productividad_data'
    __table_args__ = {'schema': 'productividad'}

    id = db.Column(db.Integer, primary_key=True)
    id_unidad_tfecha = db.Column(db.String(50))
    año = db.Column(db.Integer)
    fecha = db.Column(db.Date)
    mes_num = db.Column(db.Integer)
    trimestre = db.Column(db.Integer)
    clues = db.Column(db.String(50))
    jurisdiccion = db.Column(db.String(50))
    mes = db.Column(db.String(50))
    municipio = db.Column(db.String(50))
    unidad = db.Column(db.String(50))
    turno = db.Column(db.String(50))
    localidad = db.Column(db.String(50))
    consultorios_medicos = db.Column(db.Integer)
    tipologia = db.Column(db.String(50))
    aportacion_nucleos = db.Column(db.Float)
    medicos_turno = db.Column(db.Integer)
    nucleos_por_turno = db.Column(db.Integer)
    razon_nuclear_turno = db.Column(db.Float)
    jornadasxunidad = db.Column(db.Float)
    remover = db.Column(db.Boolean)
    consultas_de_unidad = db.Column(db.Float)


