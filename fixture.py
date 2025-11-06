# fixture.py

def obtener_inscriptos_por_juego_tribu(conexion, id_juego, tribu):
    """
    Helper que busca nombres de inscriptos para un juego y tribu específicos.
    """
    try:
        cursor = conexion.cursor()
        query = """
            SELECT u.nombre_usuario, u.apellido_usuario 
            FROM usuarios u
            JOIN inscripciones i ON u.idUsuarios = i.Usuarios_idUsuarios
            WHERE i.Juegos_idJuegos = %s AND u.tribu_usuario = %s
        """
        
        cursor.execute(query, (id_juego, tribu))
        
        nombres = [f"{nombre} {apellido}" for (nombre, apellido) in cursor.fetchall()]
        cursor.close()
        return nombres
        
    except Exception as e:
        print(f"Error obteniendo inscriptos para el fixture: {e}")
        return []


def mostrarFixture(conexion):
    """
    Muestra el fixture de todos los juegos, consultando la BBDD.
    """
    print("\n==== Fixture de juegos ====")

    try:
        cursor_juegos = conexion.cursor()
        # CORRECCIÓN: Cambiamos 'nombre' por 'nombre_juego'
        cursor_juegos.execute("SELECT idJuegos, nombre_juego FROM juegos ORDER BY idJuegos")
        juegos = cursor_juegos.fetchall()
        cursor_juegos.close()
    except Exception as e:
        print(f"Error al cargar la lista de juegos: {e}")
        return

    if not juegos:
        print("No hay juegos cargados en la base de datos.")
        return

    for (id_juego, nombre_juego) in juegos:
        
        print(f"\n --- {nombre_juego.upper()} ---")
        
        print("\nTribu Verde:")
        inscriptos_verde = obtener_inscriptos_por_juego_tribu(conexion, id_juego, "Verde")
        if not inscriptos_verde:
            print(" - (Sin inscriptos)")
        else:
            for n in inscriptos_verde:
                print(" -", n)

        print("\n===== VS =====\n")        
        
        print("Tribu Azul:")
        inscriptos_azul = obtener_inscriptos_por_juego_tribu(conexion, id_juego, "Azul")
        if not inscriptos_azul:
            print(" - (Sin inscriptos)")
        else:
            for n in inscriptos_azul:
                print(" -", n)
        
        print("\n" + "="*20)