import random



matrizJuego=[[["",1], ["",2], ["",3]], 
             [["",4], ["x",5], ["",6]], 
             [["",7], ["",8], ["",9]]]

ocupados=[5]
def verificar_ganador(matriz):
    for fila in matriz:
        simbolo = fila[0][0]
        if simbolo != "" and simbolo == fila[1][0] == fila[2][0]:
            return simbolo

    for col in range(3):
        simbolo = matriz[0][col][0]
        if simbolo != "" and simbolo == matriz[1][col][0] == matriz[2][col][0]:
            return simbolo

    simbolo_diag1 = matriz[0][0][0]
    if simbolo_diag1 != "" and simbolo_diag1 == matriz[1][1][0] == matriz[2][2][0]:
        return simbolo_diag1

    simbolo_diag2 = matriz[0][2][0]
    if simbolo_diag2 != "" and simbolo_diag2 == matriz[1][1][0] == matriz[2][0][0]:
        return simbolo_diag2
    return None


def mostrar_menu():
    while True:
        print("\n--- TIC TAC TOE ---")
        print("1. Jugar")
        print("2. Salir")
        
        opcion = input("Selecciona una opción (1 o 2): ").strip()

        if opcion == "1":
            return True  
        elif opcion == "2":
            return False  
        else:
            print("Opción inválida. Por favor, ingresa 1 o 2.")


def imprimir_tablero(matriz):
    print("\n")
    for i, fila in enumerate(matriz):
        
        celda1 = fila[0][0] if fila[0][0] != "" else fila[0][1]
        celda2 = fila[1][0] if fila[1][0] != "" else fila[1][1]
        celda3 = fila[2][0] if fila[2][0] != "" else fila[2][1]
        
        
        print(f" {celda1} | {celda2} | {celda3} ")
        
        if i < 2:
            print("---|---|---")
    print("\n")



def elegir_casilla_ia(opciones_ocupadas):
    
    disponibles = [num for num in range(1, 10) if num not in opciones_ocupadas]
    
    
    if disponibles:
        return random.choice(disponibles)
    
    return None

quiere_jugar = mostrar_menu()

if quiere_jugar:
    print("\n¡Iniciando el juego de tic-tac-toe!")

    while True:
        imprimir_tablero(matrizJuego)
        
        ganador = verificar_ganador(matrizJuego)
        if(ganador=="o"):
            print("¡Felicidades! Has ganado.")
            break
        if(ganador=="x"):
            print("La maquina ha ganado. lastima!")
            break
        elif len(ocupados) == 9:
            print("¡Es un empate! No quedan más posiciones.")
            break

        try:
            respuestaP = int(input("Ingrese la posición (1-9): "))
        except ValueError:
            print("Entrada inválida. Debe ser un número entero.")
            continue

        if(respuestaP <0 or respuestaP >9):
            print("Posición inválida. Por favor, ingresa un número del 1 al 9.")
            continue
        
        for i in matrizJuego:
            for j in i:
                if j[1] == respuestaP:
                    if j[0] == "":
                        j[0] = "o"
                        ocupados.append(respuestaP)
                    else:
                        print("Posición ocupada. Por favor, elige otra posición.")
                        break
            else:
                continue
            break

        imprimir_tablero(matrizJuego)

        ganador = verificar_ganador(matrizJuego)
        if(ganador=="o"):
            print("¡Felicidades! Has ganado.")
            break
        if(ganador=="x"):
            print("La maquina ha ganado. lastima!")
            break
        elif len(ocupados) == 9:
            print("¡Es un empate! No quedan más posiciones.")
            break

        x = elegir_casilla_ia(ocupados)
        if x is not None:
            for i in matrizJuego:
                for j in i:
                    if j[1] == x:
                        j[0] = "x"
                        ocupados.append(x)
                        break
                else:
                    continue
                break




    # -------
else:
    print("\nGracias por participar. ¡Hasta luego!")
