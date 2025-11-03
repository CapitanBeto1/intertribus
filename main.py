from inscripciones import inscribirUsuario
from fixture import mostrarFixture
from tribus import mostrarInscriptos

# menu
def main(): 
    while True:
        print("\n==== Menú Principal ====")
        print("1. Inscribirse en un juego")
        print("2. Ver fixture de juegos")
        print("3. Ver inscriptos por tribu")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            inscribirUsuario()
        elif opcion == "2":
            mostrarFixture()
        elif opcion == "3":
            mostrarInscriptos()
        elif opcion == "0":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()