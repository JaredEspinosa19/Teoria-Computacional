import random
"""
Gramatica libres de contexto
Palindromos
"""

if __name__ == "__main__":

    #INICIO PROGRAMA

    print("--------PROGRAMA QUE GENERA PALINDROMOS--------")
    print("Seleccione la opción deseada:")
    print("1 - Digitar la longitud del palindromo")
    print("2 - Generar la longitud aleatoriamente")

    opcion = 0

    opcion = int(input(""))
    longitud = 0
    
    if opcion == 1:
        longitud = int(input("Digite la longitud: "))
    else:
        longitud = random.randint(0,100000)

    print(f"Longitud del palindromo = {longitud}")

    aux = 0
    palindromo = "" 

    file = open("P6\\Palindromo.txt", "w", encoding="UTF-8")

    while aux < longitud:

        if (longitud - aux) > 2:
            sel = random.randint(4,5)
            if sel==4: #P -> 0P0
                palindromo = palindromo[:int(aux/2)]+ "0P0" + palindromo[(-1)*int(aux/2):]
                print( "P -> 0P0 | " + palindromo)
                file.write("P -> 0P0 | " + palindromo + "\n")
            elif sel==5: # P -> 1P1
                palindromo = palindromo[:int(aux/2)]+ "1P1" + palindromo[(-1)*int(aux/2):]
                print( "P -> 1P1 | " + palindromo)
                file.write("P -> 1P1 | " + palindromo + "\n")
            aux+=2
        else:
            n = (longitud - aux)%2
            sel = random.randint(1,3)

            if sel==1: #P -> e
                palindromo = palindromo[:int(aux/2)]+ "ϵ"*(2-n) + palindromo[(-1)*int(aux/2):]
                print( "P -> ϵ | " + palindromo)
                file.write("P -> ϵ | " + palindromo + "\n")
            elif sel==2: #P -> 0
                palindromo = palindromo[:int(aux/2)]+ "0"*(2-n) + palindromo[(-1)*int(aux/2):]
                print( "P -> 0 | " + palindromo)
                file.write("P -> 0 | " + palindromo + "\n")
            else: #P -> 1
                palindromo = palindromo[:int(aux/2)]+ "1"*(2-n) + palindromo[(-1)*int(aux/2):]
                print( "P -> 1 | " + palindromo)
                file.write("P -> 1 | " + palindromo + "\n")
            
            
            aux = aux + (2-n)
    
    print("----PALINDROMO GENERADO------")
    print(palindromo)
    file.write(palindromo)

    file.close()
