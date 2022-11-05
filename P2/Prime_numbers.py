import matplotlib.pyplot as plt

NS = 8000000#200^3

ARCHIVO="P2\\Prime_numbers.txt"

def plotOnes(x,y):    
    
    plt.plot(x,y,color="green")
    #plt.axhline(0, color='black')
    #plt.axvline(0, color='black')
    plt.xlabel('Numero')
    plt.ylabel('Numero 1s en Binario')
    plt.title("Gráfica")
    #plt.savefig('P2\\plot_primes.png')
    plt.show()

def writeFile(list):

    with open(ARCHIVO,"w") as file:
        file.write('{')
        for x in list:
            file.write("{}".format(x)+",")
        file.write('}')

def countOnes(list):

    frequency=[]

    for x in list:
        aux = (format(x,"b"))
        frequency.append(aux.count("1"))
        
    return frequency

def calculatePrimes(NP):

    #Criba de erastotenes
    array = list(range(1,NS+1)) 
    aux=1

    while True:
        #obtenemos el primer elemento
        first = array[aux]
        #removemos los multiplos del arreglo principal
        array = [elem for elem in array if elem%first !=0 or elem==first]
        if(array[aux+1]**2 < NS):
            aux=aux+1
            continue
        else:
            break

    
    return array

if __name__ == "__main__":
    primes=calculatePrimes(NS)  
    ones=countOnes(primes)

    #print(primes)
    plotOnes(primes,ones)
    writeFile(primes)
