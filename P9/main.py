import Turing_machine as TM
import random
import animation

def generateString():
    cadena = ""
    N = random.randint(2, 1000)
    for i in range(N):
        aux = random.randint(0, 1)
        cadena = cadena + str(aux)  

    return cadena


if __name__ == "__main__":

    Turing_machine = TM.TM()

    print("Programa que evalua si una cadena es válida mediante un máquina de Touring")
    print("Escoja la opción que desea ejecutar")
    print("1 - Ingresar cadena")
    print("2 - Generar cadena")
    opc = int(input())
    cadena = ""
    if opc == 1:
        print("Introduzca la cadena") 
        cadena = input()
    else:
        print("Generando cadena")
        cadena = generateString()

    cadena = "BBB" + cadena + "BBB"

    cadena = [i for i in cadena]

    aux = True
    counter = 3

    file = open("P9\\MaquinaTuring.txt", "w", encoding="UTF-8")
    
    states = []

    while aux:

        #Imprimir descripción directa
        f = "".join(cadena[:counter])
        d = "".join(cadena[counter:])
        states.append([f, d])     
        print(f + " " + Turing_machine.get_estado_actual()+ " " + d)
        file.write(f + " " + Turing_machine.get_estado_actual()+ " " + d + "\n")
        char, index, aux = Turing_machine.siguiente_estado(cadena[counter])

        cadena[counter] = char
        counter = counter + index

    file.close()
    #Checar si es cadena válida
    if Turing_machine.get_estado_actual() == 'q4':
        print("Cadena váilida")
    else:
        print("Cadena inválida")

    ###Animation
    if len(cadena)-6 <= 10:
        window = animation.Board(500, 500)
        window(states) 