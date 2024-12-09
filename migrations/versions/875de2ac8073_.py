"""empty message

Revision ID: 875de2ac8073
Revises: ffc50a05895a
Create Date: 2024-12-05 15:18:07.912345

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '875de2ac8073'
down_revision = 'ffc50a05895a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('productividad_data')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('productividad_data',
    sa.Column('ID_unidad_tfecha', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('Año', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('Fecha', sa.DATE(), nullable=True),
    sa.Column('Mes_num', mysql.TINYINT(), autoincrement=False, nullable=True),
    sa.Column('Trimestre', mysql.VARCHAR(length=10), nullable=True),
    sa.Column('Clues', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('Jurisdiccion', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('Mes', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('Municipio', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('Unidad', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('Turno', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('Localidad', mysql.VARCHAR(length=50), nullable=True),
    sa.Column('Consultorios_Medicos', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('Tipologia', mysql.VARCHAR(length=100), nullable=True),
    sa.Column('Aportacion_de_nucleos', mysql.FLOAT(), nullable=True),
    sa.Column('Medicos_Turno', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('Nucleos_por_turno', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('Razon_nuclear_turno', mysql.FLOAT(), nullable=True),
    sa.Column('JornadasxUnidad', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('Remover', mysql.FLOAT(), nullable=True),
    sa.Column('Consultas_de_unidad', mysql.INTEGER(), autoincrement=False, nullable=True),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
