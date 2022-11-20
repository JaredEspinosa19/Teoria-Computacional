import matplotlib.pyplot as plt
import math

NS = 8000000#200^3

ARCHIVO_B="P2\\Prime_numbers_binary.txt"
ARCHIVO_D="P2\\Prime_numbers_decimal.txt"


def plotOnes(x,y):    
    #Grafica numeros 1
    plt.plot(x,y,color="green")
    plt.xlabel('Cadena')
    plt.ylabel('Números 1s')
    plt.title("Gráfica")
    #plt.savefig('P2\\plot_primes.png')
    plt.show()

    #Grafica logaritmo 2
    plt.plot(x,[math.log(i,2) for i in y],color="green")
    plt.xlabel('Cadena')
    plt.ylabel('Valor Números 1s en logaritmo base 2')
    plt.title("Gráfica")
    #plt.savefig('P2\\plot_log2.png')
    plt.show()

    #Grafica logarimo 10
    plt.plot(x,[math.log(i,10) for i in y],color="green")
    plt.xlabel('Cadena')
    plt.ylabel('Valor Números 1s en logaritmo base 10')
    plt.title("Gráfica")
    #plt.savefig('P2\\plot_log10.png')
    plt.show()

def writeFile(list):

    with open(ARCHIVO_D,"w") as file:
        file.write('{')
        for x in list:
            file.write("{}".format(x)+",")
        file.write('}')

    with open(ARCHIVO_B,"w") as file:
        file.write('{')
        for x in list:
            file.write(format(x,'b')+",")
        file.write('}')

def countOnes(list):

    frequency=[]

    for x in list:
        aux = (format(x,"b"))
        frequency.append(aux.count("1"))
        
    return frequency

def calculatePrimes(NP):
    #Criba de erastotenes
    array = list(range(1,NP+1)) 
    aux=1

    while True:
        #obtenemos el primer elemento
        first = array[aux]
        array = [elem for elem in array if elem%first !=0 or elem==first]
        if(array[aux+1]**2 < NP):
            aux=aux+1
            continue
        else:
            break
    
    return array

if __name__ == "__main__":
    
    while True:
        n = int(input("Escriba el número hasta el que desea calcular los número primos: "))
        primes=calculatePrimes(n)  
        ones=countOnes(primes)
        writeFile(primes)
        plotOnes(primes,ones)

        if(input("Calcular de nuevo: \n No = N \n Si = cualquier tecla \n").lower()== "n"):
            break
        else:
            continue