# funciones_auxiliares.py

# ... (obtener_carreras y pedirDatosUsuario quedan igual que antes) ...

def obtener_carreras(conexion):
    """Función helper para traer las carreras de la BBDD."""
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT idCarreras, nombre_carreras FROM carreras ORDER BY idCarreras")
        carreras = cursor.fetchall() 
        cursor.close()
        return carreras
    except Exception as e:
        print(f"Error al obtener carreras: {e}")
        return []

def pedirDatosUsuario(conexion):
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ") 
    
    while True:
        genero_op = input("Ingresa tu género (1. Masculino / 2. Femenino): ")
        if genero_op == "1":
            genero = "Masculino"
            break
        elif genero_op == "2":
            genero = "Femenino"
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

    while True:
        tribu_op = input("Ingresa tu tribu (1. Verde / 2. Azul): ")
        if tribu_op == "1":
            tribu = "Verde"
            break
        elif tribu_op == "2":
            tribu = "Azul"
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

    carreras = obtener_carreras(conexion)
    if not carreras:
        print("Error: No se pudieron cargar las carreras. Usando ID '1' por defecto.")
        return nombre, apellido, genero, tribu, 1 

    print("\nSelecciona tu carrera:")
    id_carreras_validos = []
    for id_c, nombre_c in carreras:
        print(f"{id_c}. {nombre_c}")
        id_carreras_validos.append(str(id_c)) 

    while True:
        carrera_id_str = input("Ingresa el NÚMERO de tu carrera: ")
        if carrera_id_str in id_carreras_validos:
            return nombre, apellido, genero, tribu, int(carrera_id_str) 
        else:
            print("Opción inválida. Intenta de nuevo.")


def mostrarJuegos(conexion): 
    print("--------------------")
    print("Juegos disponibles:")
    print("--------------------")
    
    try:
        cursor = conexion.cursor()
        
        # CORRECCIÓN: Cambiamos 'nombre' por 'nombre_juego'
        query = "SELECT idJuegos, nombre_juego, cupos_verde, cupos_azul FROM juegos ORDER BY idJuegos"
        cursor.execute(query)
        
        juegos = cursor.fetchall()
        if not juegos:
            print("No hay juegos cargados en la base de datos.")
            print("(Asegúrate de ejecutar el INSERT de los juegos en phpMyAdmin)")
            cursor.close()
            return

        for (id_juego, nombre, cupos_v, cupos_a) in juegos:
            print(f"{id_juego}. {nombre.upper()}. Cupos verde: {cupos_v}, Cupos azul: {cupos_a}")
        
        print("0. Volver al menú principal")
        cursor.close()

    except Exception as e:
        print(f"Error al mostrar juegos: {e}")