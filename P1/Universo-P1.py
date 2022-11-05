ALPHABET=["0","1"]
ARCHIVO="Universe.txt"

import matplotlib.pyplot as plt
import math

def writeFile(list):
    with open(ARCHIVO,"w") as file:
        for x in list:
            file.write(x+",")

def plot(x,y):
    
    plt.plot(x,y,color="red")
    # Pintamos lineas que pasan por el origen de coordenadas
    #plt.axhline(0, color='black')
    #plt.axvline(0, color='black')
    # Fijamos límites, etiquetas y títulos
    plt.xlabel('Cadena')
    plt.ylabel('Numero 1s')
    plt.title("Gráfica")
    plt.show()

def plot_log(x,y):
    plt.plot(x,y,color="red")
    # Pintamos lineas que pasan por el origen de coordenadas
    #plt.axhline(0, color='black')
    #plt.axvline(0, color='black')
    # Fijamos límites, etiquetas y títulos
    plt.xlabel('Cadena')
    plt.ylabel('Valor logaritmo base 10 de 1s')
    plt.title("Gráfica logaritmo base 10")
    plt.show()


def countOne(list):
    frequency=[]
    for i in list:
        frequency.append(i.count("1"))
    return frequency

def createUniverse(alphabet,k):
    universe=["e"]+alphabet
    mem = alphabet
    for i in range(1,k):
        mem = ["0"+i for i in mem] + ["1"+i for i in mem]
        universe = universe + mem
    return universe

def main():
    while True:
        n= int(input("Introduzca N: "))    
        result=createUniverse(ALPHABET,n)
        ones=countOne(result)
        #log = [math.log(i,10)  if i!=0 else 0 for i in ones]
        #print(ones)
        #print(log)
        plot(list(range(0,len(ones))),ones)
        #plot_log(list(range(0,len(ones))),log)
        #writeFile(result)

        if(input("Desea ejecutar de nuevo \n SI = S \n NO = N: "))=="N":
            break

if __name__ == "__main__":
    main()


