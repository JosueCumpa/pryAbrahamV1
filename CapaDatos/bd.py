# import pymysql
import psycopg2


def obtener_conexion():
    return psycopg2.connect(host='127.0.0.1',
                        port=5432,
                        user='postgres',
                        password='12',
                        database='bd_prediccion')

# si no tienen postgres instalado pueden usar esta bd online

#def obtener_conexion():
#    return psycopg2.connect(host='jelani.db.elephantsql.com',
#                            port=5432,
#                            user='nzsbwaov',
#                            password='KGMLF1yVbv70Y7GqkfPRPVNL0C0GWQ2O',
#                            database='nzsbwaov')