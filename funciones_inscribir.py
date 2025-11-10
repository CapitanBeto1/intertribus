# funciones_inscribir.py

def inscribir(conexion, id_usuario, tribu, juego_id):
    """
    Inscribe a un usuario en un juego usando la BBDD.
    Utiliza una transacción para asegurar la integridad de los datos.
    """
    
    columna_cupo = "cupos_verde" if tribu == "Verde" else "cupos_azul"
    
    cursor = conexion.cursor(buffered=True)
    
    try:
        cursor.execute("START TRANSACTION")
        
        # CORRECCIÓN: Cambiamos 'nombre' por 'nombre_juego'
        # ¡Asegúrate que 'cupos_verde' y 'cupos_azul' sean correctos!
        query_juego = f"SELECT nombre_juego, {columna_cupo} FROM juegos WHERE idJuegos = %s FOR UPDATE"
        cursor.execute(query_juego, (juego_id,))
        
        juego = cursor.fetchone()
        
        if juego is None:
            print(f"Error: El juego con ID {juego_id} no existe.")
            cursor.execute("ROLLBACK") 
            cursor.close()
            return False, ""
            
        nombre_juego_str = juego[0] # El nombre ya está aquí
        cupos_disponibles = juego[1]
        
        if cupos_disponibles > 0:
            
            query_update = f"UPDATE juegos SET {columna_cupo} = {columna_cupo} - 1 WHERE idJuegos = %s"
            cursor.execute(query_update, (juego_id,))
            
            query_insert = """
                INSERT INTO inscripciones (Usuarios_idUsuarios, Juegos_idJuegos, fecha_inscripciones) 
                VALUES (%s, %s, NOW())
            """
            cursor.execute(query_insert, (id_usuario, juego_id))
            
            cursor.execute("COMMIT")
            cursor.close()
            return True, nombre_juego_str # Devolvemos el nombre que obtuvimos
            
        else:
            print(f"Lo sentimos, no quedan cupos para '{nombre_juego_str}' en la tribu {tribu}.")
            cursor.execute("ROLLBACK")
            cursor.close()
            return False, nombre_juego_str

    except Exception as e:
        print(f"Error al inscribir: {e}")
        cursor.execute("ROLLBACK") 
        cursor.close()
        return False, ""