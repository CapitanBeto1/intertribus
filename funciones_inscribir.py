from datos import *

def obtenerIndiceTribu(tribu):
    if tribu == "Verde":
        return 0
    else:   # tribu == "Azul"
        return 1
    
def inscribir(nombre, tribu, juego):
    i = obtenerIndiceTribu(tribu)

    if juego == "1":    # Ajedrez
        inscriptosAjedrez.append((nombre, tribu))
        cuposAjedrez[i] -= 1
        return True, "Ajedrez" 
    
    elif juego == "2":  # Truco
        inscriptosTruco.append((nombre, tribu))
        cuposTruco[i] -= 1
        return True, "Truco"
    
    elif juego == "3":  # Habilidades
        inscriptosHabilidades.append((nombre, tribu))
        cuposHabilidades[i] -= 1
        return True, "Habilidades"
    
    elif juego == "4":  # Tutti Frutti
        inscriptosTuttiFrutti.append((nombre, tribu))
        cuposTuttiFrutti[i] -= 1
        return True, "Tutti Frutti"
    
    return False, ""  # Juego no válido