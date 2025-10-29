cuposAjedrezVerde=1
cuposTrucoVerde=2
cuposHabilidadesVerde=5
cuposTuttiFruttiVerde=4
#a
cuposAjedrezAzul=1
cuposTrucoAzul=2
cuposHabilidadesAzul=5
cuposTuttiFruttiAzul=4

inscriptosAjedrez=[]
inscriptosTruco=[]
inscriptosHabilidades=[]
inscriptosTuttiFrutti=[]

while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Inscribirse a juegos")
    print("2. Ver fixture de juegos")
    print("3. Ver inscriptos por tribu")
    print("0. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        nombreUsuario=input("Ingresa tu nombre: ")
        generoUsuario=input("Ingresa tu genero: 1. Masculino 2. Femenino\n")
        tribuUsuario=input("Ingresa tu tribu: 1. Verde 2. Azul\n")

        if tribuUsuario=="1":
            tribuUsuario="Verde"
        elif tribuUsuario=="2":
            tribuUsuario="Azul"

        if generoUsuario=="1":  
            generoUsuario="Masculino"
        elif generoUsuario=="2":
            generoUsuario="Femenino"

        juegoSeleccionado=""
        inscripcionUsuario=0

        while juegoSeleccionado!="0":
            print("--------------------")
            print("Juegos disponibles:")
            print("--------------------")
            print("1. AJEDREZ. Cupos verde: ", cuposAjedrezVerde, " Cupos azul: ", cuposAjedrezAzul)
            print("2. TRUCO. Cupos verde: ", cuposTrucoVerde, " Cupos azul: ", cuposTrucoAzul)
            print("3. HABILIDADES. Cupos verde: ", cuposHabilidadesVerde, " Cupos azul: ", cuposHabilidadesAzul)
            print("4. TUTTI FRUTTI. Cupos verde: ", cuposTuttiFruttiVerde, " Cupos azul: ", cuposTuttiFruttiAzul)
            print("--------------------")
            print("Volver al menú principal: 0")

            juegoSeleccionado=input("Selecciona el juego al que deseas inscribirte (1-4): ")

            match juegoSeleccionado:
                case "1":
                    if tribuUsuario=="Verde" and cuposAjedrezVerde>0:
                        inscriptosAjedrez.append((nombreUsuario, tribuUsuario))
                        inscripcionUsuario+=1
                        cuposAjedrezVerde-=1
                        print(nombreUsuario, ", te has inscrito correctamente al juego de Ajedrez.")
                    elif tribuUsuario=="Azul" and cuposAjedrezAzul>0:
                        inscriptosAjedrez.append((nombreUsuario, tribuUsuario))
                        inscripcionUsuario+=1
                        cuposAjedrezAzul-=1
                        print(nombreUsuario, ", te has inscrito correctamente al juego de Ajedrez.")
                    else:
                        print("No hay cupos disponibles para Ajedrez en tu tribu.")

                case "2":
                    if tribuUsuario=="Verde" and cuposTrucoVerde>0:
                        inscriptosTruco.append((nombreUsuario, tribuUsuario))
                        inscripcionUsuario+=1
                        cuposTrucoVerde-=1
                        print(nombreUsuario, ", te has inscrito correctamente al juego de Truco.")
                    elif tribuUsuario=="Azul" and cuposTrucoAzul>0:
                        inscriptosTruco.append((nombreUsuario, tribuUsuario))
                        inscripcionUsuario+=1
                        cuposTrucoAzul-=1
                        print(nombreUsuario, ", te has inscrito correctamente al juego de Truco.")
                    else:
                        print("No hay cupos disponibles para Truco en tu tribu.")

                case "3":
                    if tribuUsuario=="Verde" and cuposHabilidadesVerde>0:
                        inscriptosHabilidades.append((nombreUsuario, tribuUsuario))
                        inscripcionUsuario+=1
                        cuposHabilidadesVerde-=1
                        print(nombreUsuario, ", te has inscrito correctamente al juego de Habilidades.")
                    elif tribuUsuario=="Azul" and cuposHabilidadesAzul>0:
                        inscriptosHabilidades.append((nombreUsuario, tribuUsuario))
                        inscripcionUsuario+=1
                        cuposHabilidadesAzul-=1
                        print(nombreUsuario, ", te has inscrito correctamente al juego de Habilidades.")
                    else:
                        print("No hay cupos disponibles para Habilidades en tu tribu.")
                        
                case "4":
                    if tribuUsuario=="Verde" and cuposTuttiFruttiVerde>0:
                        inscriptosTuttiFrutti.append((nombreUsuario, tribuUsuario))
                        inscripcionUsuario+=1
                        cuposTuttiFruttiVerde-=1
                        print(nombreUsuario, ", te has inscrito correctamente al juego de Tutti Frutti.")
                    elif tribuUsuario=="Azul" and cuposTuttiFruttiAzul>0:
                        inscriptosTuttiFrutti.append((nombreUsuario, tribuUsuario))
                        inscripcionUsuario+=1
                        cuposTuttiFruttiAzul-=1
                        print(nombreUsuario, ", te has inscrito correctamente al juego de Tutti Frutti.")
                    else:
                        print("No hay cupos disponibles para Tutti Frutti en tu tribu.")
            if inscripcionUsuario>=3:
                print("Has alcanzado el máximo de inscripciones permitidas.")
                print("Juegos a los que ", nombreUsuario, " está inscrito:", inscripcionUsuario)
                break
    elif opcion == "2":
        verdesAjedrez = []
        azulesAjedrez = []
        print("FIXTURE DE JUEGOS")
        print("----------------------------------")
        print("AJEDREZ:\n")
        print("----------------------------------")
        for jugador in inscriptosAjedrez:
            if jugador[1] == "Verde":
                verdesAjedrez.append(jugador[0])
            else:
                azulesAjedrez.append(jugador[0])
        print("Tribu Verde:", verdesAjedrez, "V.S", "Tribu Azul:", azulesAjedrez)
        print("----------------------------------")

        verdesTruco = []
        azulesTruco = []
        print("TRUCO:\n")
        print("----------------------------------")
        for jugador in inscriptosTruco:
            if jugador[1] == "Verde":
                verdesTruco.append(jugador[0])
            else:
                azulesTruco.append(jugador[0])
        print("Tribu Verde:", verdesTruco, "V.S", "Tribu Azul:", azulesTruco)
        print("----------------------------------")

        verdesHabilidades = []
        azulesHabilidades = []
        print("HABILIDADES:\n")
        print("----------------------------------")
        for jugador in inscriptosHabilidades:
            if jugador[1] == "Verde":
                verdesHabilidades.append(jugador[0])
            else:
                azulesHabilidades.append(jugador[0])
        print("Tribu Verde:", verdesHabilidades, "V.S", "Tribu Azul:", azulesHabilidades)
        print("----------------------------------")

        verdesTuttiFrutti = []
        azulesTuttiFrutti = []

        print("TUTTI FRUTTI:\n")
        print("----------------------------------")
        for jugador in inscriptosTuttiFrutti:
            if jugador[1] == "Verde":
                verdesTuttiFrutti.append(jugador[0])
            else:
                azulesTuttiFrutti.append(jugador[0])
        print("Tribu Verde:", verdesTuttiFrutti, "V.S", "Tribu Azul:", azulesTuttiFrutti)
        print("----------------------------------")

    elif opcion == "3":
        print("\nINSCRIPTOS POR TRIBU")
        print("--------------------")
        
        print("\nTribu Verde:")
        print("--------------------")
        print("AJEDREZ:")
        for jugador in inscriptosAjedrez:
            if jugador[1] == "Verde":
                print(jugador[0])
                
        print("\nTRUCO:")
        for jugador in inscriptosTruco:
            if jugador[1] == "Verde":
                print(jugador[0])
                
        print("\nHABILIDADES:")
        for jugador in inscriptosHabilidades:
            if jugador[1] == "Verde":
                print(jugador[0])
                
        print("\nTUTTI FRUTTI:")
        for jugador in inscriptosTuttiFrutti:
            if jugador[1] == "Verde":
                print(jugador[0])
                
        print("--------------------")
        print("\nTribu Azul:")
        print("--------------------")
        print("AJEDREZ:")
        for jugador in inscriptosAjedrez:
            if jugador[1] == "Azul":
                print(jugador[0])
                
        print("\nTRUCO:")
        for jugador in inscriptosTruco:
            if jugador[1] == "Azul":
                print(jugador[0])
                
        print("\nHABILIDADES:")
        for jugador in inscriptosHabilidades:
            if jugador[1] == "Azul":
                print(jugador[0])
                
        print("\nTUTTI FRUTTI:")
        for jugador in inscriptosTuttiFrutti:
            if jugador[1] == "Azul":
                print(jugador[0])
        
        print("--------------------")
