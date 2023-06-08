
from CapaDatos.bd import obtener_conexion
from werkzeug.security import check_password_hash,generate_password_hash

password='1234' # contraseña por defecto para generar el hash
#password_hash = generate_password_hash(password, method='sha256')

# Verificar si una contraseña es correcta
def check_password(hashed_password, password):
    return check_password_hash(hashed_password, password)

#print(password_hash) #saber la contraseña por defecto para generar el hash

# Verificar si una contraseña ingresada es correcta
def login(username, password):
    conexion = obtener_conexion()
    user = []
    with conexion.cursor() as cursor:
        cursor.execute(
            "select * from fn_login(%s)", (username, ),
        )
        row = cursor.fetchone()
    conexion.close()
    if row == None:
        return None
    else:
        user = [
            row[0],
            row[1],
            row[2],
            row[3],
            check_password(row[4], password),
            row[5],
            row[6],
            row[7],
        ]
    return user