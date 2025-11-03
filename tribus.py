from datos import *

def mostrarInscriptos():
    print("==== Inscriptos ====")

    for tribu in ["Verde", "Azul"]:
        print("\nTribu", tribu)
        print("-------------------")

        print("Ajedrez:")
        for n, t in inscriptosAjedrez:
            if t == tribu:
                print(" -", n)
        
        print("Truco:")
        for n, t in inscriptosTruco:
            if t == tribu:
                print(" -", n)

        print("Habilidades:")
        for n, t in inscriptosHabilidades:
            if t == tribu:
                    print(" -", n)

        print("Tutti Frutti:")
        for n, t in inscriptosTuttiFrutti:
            if t == tribu:
                print(" -", n)