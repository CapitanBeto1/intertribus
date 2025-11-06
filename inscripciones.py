# inscripciones.py

from funciones_auxiliares import pedirDatosUsuario, mostrarJuegos
from funciones_inscribir import inscribir 

def guardar_usuario(conexion, nombre, apellido, genero, tribu, id_carrera):
    """Guarda el nuevo usuario en la BBDD y retorna su ID."""
    try:
        cursor = conexion.cursor()
        query = """
            INSERT INTO usuarios 
            (nombre_usuario, apellido_usuario, genero_usuario, tribu_usuario, Carreras_idCarreras) 
            VALUES (%s, %s, %s, %s, %s)
        """
        datos_usuario = (nombre, apellido, genero, tribu, id_carrera)
        
        cursor.execute(query, datos_usuario)
        conexion.commit() 
        
        nuevo_id = cursor.lastrowid 
        print(f"Usuario '{nombre} {apellido}' registrado con ID: {nuevo_id}.")
        cursor.close()
        return nuevo_id
        
    except Exception as e:
        print(f"Error al guardar usuario: {e}")
        conexion.rollback() 
        cursor.close()
        return None

def contar_inscripciones(conexion, id_usuario):
    """Cuenta en cuántos juegos está inscripto un usuario."""
    try:
        cursor = conexion.cursor(buffered=True) 
        # CORRECCIÓN: Usamos la columna 'Usuarios_idUsuarios'
        query = "SELECT COUNT(*) FROM inscripciones WHERE Usuarios_idUsuarios = %s"
        cursor.execute(query, (id_usuario,))
        
        conteo = cursor.fetchone()[0] 
        cursor.close()
        return conteo
        
    except Exception as e:
        print(f"Error al contar inscripciones: {e}")
        cursor.close()
        return 0 

def inscribirUsuario(conexion): 
    
    nombre, apellido, genero, tribu, carrera_id = pedirDatosUsuario(conexion)
    id_usuario = guardar_usuario(conexion, nombre, apellido, genero, tribu, carrera_id)
    
    if id_usuario is None:
        print("No se pudo registrar al usuario. Volviendo al menú.")
        return

    inscripciones = contar_inscripciones(conexion, id_usuario)
    print(f"Ya tienes {inscripciones} inscripciones.")

    while inscripciones < 3:
        mostrarJuegos(conexion) 
        juego_id = input("Selecciona el juego al que deseas inscribirte (o 0 para salir):  ")

        if juego_id == "0":
            break

        # Pasamos el id_usuario (PK de usuarios) y el juego_id (PK de juegos)
        exito, nombreJuego = inscribir(conexion, id_usuario, tribu, juego_id)

        if exito:
            inscripciones += 1 
            print(f"Te inscribiste correctamente en {nombreJuego}. Total inscripciones: {inscripciones}/3")
        else:
            print("Intenta con otro juego.")
        
        if inscripciones == 3:
            print("Alcanzaste el maximo de inscripciones permitidas (3).")