ALPHABET=["0","1"]
ARCHIVO="P1\\Universe.txt"
ARCHIVO2="P1\\Universe_64.txt"

import matplotlib.pyplot as plt
import math

def writeFile1(list):
    with open(ARCHIVO,"w") as file:
        file.write("{")
        for x in list:
            file.write(x+",")
        file.write("{")

def writeFile64(list):
    
    cadena = ""
    with open(ARCHIVO2,"w") as file:
        for x in list:
            
            if((len(cadena)+len(x))>64):
              dif = 64 -len(cadena)
              cadena=cadena + x[:dif] + '\n'
              file.write(cadena)
              cadena=x[dif:]  
            #si ya tiene 64 bits
            elif((len(cadena)+len(x))==64):
                cadena = cadena + x + "\n"
                file.write(cadena)
                cadena=""
            else:
                cadena = cadena + x


def plot(ones,ones64):
    
    #Numeros 1's
    plt.plot(list(range(0,len(ones))),ones,color="red")
    plt.xlabel('Cadena')
    plt.ylabel('Numeros 1s')
    plt.title("Gráfica")
    #plt.savefig('P1\\plot_1s.png')
    plt.show()

    ones.clear()
    #Numeros de unos en cadenas de 64 bits
    plt.plot(list(range(0,len(ones64))),ones64,color="red")
    plt.xlabel('Cadena')
    plt.ylabel('Numeros 1s en cadenas 64 bits')
    plt.title("Gráfica")
    #plt.savefig('P1\\plot_64.png')
    plt.show()

    #Numeros de unos en cadenas de 64 bits evaluados en log10
    plt.plot(list(range(0,len(ones64))),[math.log(i,10) for i in ones64],color="red")
    plt.xlabel('Cadena')
    plt.ylabel('Numeros 1s en cadenas 64 bits evaluado en logaritmo base 10')
    plt.title("Gráfica")
    #plt.savefig('P1\\plot_64log.png')
    plt.show()

def count64():
    
    with open(ARCHIVO2) as file:
        frequency = [linea.count("1") for linea in file]        
    
    return frequency

def countOne(list):
    frequency=[ (i.count("1")) for i in list]
    list.clear()
    return frequency

def createUniverse(alfabeto,n):
    uv=["e"]+alfabeto
    mem = alfabeto
    for i in range(1,n):
        mem = ["0"+i for i in mem] + ["1"+i for i in mem]
        uv = uv + mem
    return uv

if __name__ == "__main__":
    
    while True:
        n = int(input("Escriba el valor de n hasta el que desea calcular el universo (Sigma^n): "))
        result = createUniverse(ALPHABET,n)
        writeFile1(result)
        writeFile64(result)

        ones=countOne(result)
        ones2=count64()

        plot(ones,ones2)

        if(input("Calcular de nuevo: \n No = N \n Si = cualquier tecla \n").lower()== "n"):
            break
        else:
            continue
