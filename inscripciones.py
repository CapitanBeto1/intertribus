from funciones_auxiliares import pedirDatosUsuario, mostrarJuegos
from funciones_inscribir import inscribir

def inscribirUsuario():
    nombre, genero, tribu, carrera = pedirDatosUsuario()
    inscripciones = 0

    while inscripciones < 3:
        mostrarJuegos()
        juego = input("Selecciona el juego al que deseas inscribirte (o 0 para salir):  ")

        if juego == "0":
            break

        exito, nombreJuego = inscribir(nombre, tribu, juego)

        if exito:
            inscripciones += 1
            print(f"Te inscribiste correctamente en {nombreJuego}. Total inscripciones: {inscripciones}/3")
        else:
            print("No hay cupos disponibles para ese juego")
        
        if inscripciones == 3:
            print("Alcanzaste el maximo de inscripciones permitidas (3).")