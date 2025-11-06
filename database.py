import mysql.connector
from mysql.connector import Error

def conectar_db():
    """
    Establece y retorna una conexión con la base de datos MySQL.
    """
    try:
        # Modifica estos valores según tu configuración local de MySQL
        conexion = mysql.connector.connect(
            host='127.0.0.1',  # Tu servidor (común: 'localhost' o '127.0.0.1')
            port=3306,         # Puerto MySQL (ajusta si usas 3307 u otro)
            user='root',       # Tu usuario de MySQL (común: 'root')
            password='',       # Tu contraseña de MySQL (déjala vacía si no tienes)
            database='juegos_inter'  # Usar la DB existente en tu servidor
        )
        
        # Verificamos si la conexión fue exitosa
        if conexion.is_connected():
            # print("Conexión a la base de datos 'juegos_intertribus' exitosa.") # Puedes descomentar esto para depurar
            return conexion

    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None