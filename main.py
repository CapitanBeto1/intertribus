from inscripciones import inscribirUsuario

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
        elif opcion == "2": # 

if __name__ == "__main__":
    main()