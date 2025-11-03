from datos import *

def mostrarFixture():
    print("\n==== Fixture de juegos ====")

    juegos = [("AJEDREZ", inscriptosAjedrez), ("TRUCO", inscriptosTruco), ("HABILIDADES", inscriptosHabilidades), ("TUTTI FRUTTI", inscriptosTuttiFrutti)]

    for nombreJuego, inscriptos in juegos:
        print(f"\n {nombreJuego}:")
        print("Tribu Verde:")
        for n, t in inscriptos:
            if t == "Verde":
                print(" -", n)

        print("===== VS =====")        
        
        print("Tribu Azul:")
        for n, t in inscriptos:
            if t == "Azul":
                print(" -", n)
