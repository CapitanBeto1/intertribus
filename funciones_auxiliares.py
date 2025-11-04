from datos import *

def pedirDatosUsuario():
    nombre = input("Ingresa tu nombre: ")
    genero = input("Ingresa tu género (1. Masculino / 2. Femenino): ")
    tribu = input("Ingresa tu tribu (1. Verde / 2. Azul): ")
    carrera = input("Ingresa tu carrera (1. Ed. Fisica / 2. Inglés / 3. Biología / 4. Matemñatica / 5. Historia / 6. Geografía / 7. Programación): ")

    if genero == "1":
        genero = "Masculino"
    elif genero == "2":
        genero = "Femenino"

    if tribu == "1":
        tribu = "Verde"
    elif tribu == "2":
        tribu = "Azul"

    return nombre, genero, tribu, carrera


def mostrarJuegos():
    print("--------------------")
    print("Juegos disponibles:")
    print("--------------------")
    print("1. AJEDREZ. Cupos verde:", cuposAjedrez[0], " Cupos azul:", cuposAjedrez[1])
    print("2. TRUCO. Cupos verde:", cuposTruco[0], " Cupos azul:", cuposTruco[1])
    print("3. HABILIDADES. Cupos verde:", cuposHabilidades[0], " Cupos azul:", cuposHabilidades[1])
    print("4. TUTTI FRUTTI. Cupos verde:", cuposTuttiFrutti[0], " Cupos azul:", cuposTuttiFrutti[1])
    print("0. Volver al menú principal")
