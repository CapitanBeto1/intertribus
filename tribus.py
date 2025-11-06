# tribus.py

def mostrarInscriptos(conexion):
    """
    Muestra todos los inscriptos, agrupados por Tribu y luego por Juego.
    """
    print("==== Inscriptos ====")
    
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
        print("No hay juegos definidos en la base de datos.")
        return

    for tribu in ["Verde", "Azul"]:
        print("\n====================")
        print("   TRIBU", tribu.upper())
        print("====================")

        for id_juego, nombre_juego in juegos:
            print(f"\n {nombre_juego}:")
            
            try:
                cursor_inscriptos = conexion.cursor()
                query = """
                    SELECT u.nombre_usuario, u.apellido_usuario
                    FROM usuarios u
                    JOIN inscripciones i ON u.idUsuarios = i.Usuarios_idUsuarios
                    WHERE u.tribu_usuario = %s AND i.Juegos_idJuegos = %s
                """
                
                cursor_inscriptos.execute(query, (tribu, id_juego))
                
                inscriptos = cursor_inscriptos.fetchall()
                cursor_inscriptos.close()
                
                if not inscriptos:
                    print(" - (Sin inscriptos)")
                else:
                    for (nombre, apellido) in inscriptos:
                        print(f" - {nombre} {apellido}")
                        
            except Exception as e:
                print(f"Error al buscar inscriptos para {nombre_juego}: {e}")