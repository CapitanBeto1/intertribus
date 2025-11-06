# Importamos las funciones de tus módulos originales
from inscripciones import inscribirUsuario
from fixture import mostrarFixture
from tribus import mostrarInscriptos

# Importamos la función de conexión del nuevo módulo
from database import conectar_db

def main():
    # 1. Conectamos a la base de datos AL INICIAR
    print("Estableciendo conexión con la base de datos...")
    conexion = conectar_db()

    # Si la conexión falla, no podemos continuar.
    if not conexion:
        print("ERROR: No se pudo conectar a la base de datos. El programa se cerrará.")
        return # Termina la función main()

    print("¡Conexión exitosa!")
    
    while True:
        print("\n==== Menú Principal ====")
        print("1. Inscribirse en un juego")
        print("2. Ver fixture de juegos")
        print("3. Ver inscriptos por tribu")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # 2. Pasamos la conexión a las funciones que la usarán
            inscribirUsuario(conexion) 
        elif opcion == "2":
            mostrarFixture(conexion)
        elif opcion == "3": 
            mostrarInscriptos(conexion)
        elif opcion == "0":
            print("Saliendo del programa.")
            break # Rompe el bucle while
        else:
            print("Opción inválida.")

    # 3. Cerramos la conexión AL SALIR (después del bucle)
    if conexion.is_connected():
        conexion.close()
        print("Conexión a la base de datos cerrada.")

if __name__ == "__main__":
    main()