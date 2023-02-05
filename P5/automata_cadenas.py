import Web_scrapping as ws

delta = {'z0':{'g':'a1', 'c':'b1,d1,e1,f1,g1', 'd':'c1,h1'},
         'a1':{'r':'a2'},
         'b1,d1,e1,f1,g1':{'a':'d2,f2', 'o':'b2,e2', 'u':'g2'},
         'c1,h1':{'i':'c2', 'o':'h2'},
         'a2':{'i':'a3'},
         'b2,e2':{'n':'b3', 'v':'e3'},
         'd2,f2':{'n':'f3', 'l':'d3'},
         'g2':{'b':'g3'},
         'c2':{'s':'c3'},
         'h2':{'l':'h3'},
         'a3':{'p':'a4'},
         'e3':{'i':'e4'},
         'd3':{'e':'d4'},
         'f3':{'s':'f4'},
         'g3':{'r':'g4'},
         'c3':{'t':'c4'},
         'h3':{'o':'h4'},
         'a4':{'a':'a5'},
         'e4':{'d':'e5'},
         'd4':{'n':'d5'},
         'f4':{'a':'f5'},
         'g4':{'e':'g5'},
         'h4':{'r':'h5'},
         'a5':{'g':'a1', 'c':'b1,d1,e1,f1,g1', 'd':'c1,h1'},
         'e5':{'g':'a1', 'c':'b1,d1,e1,f1,g1', 'd':'c1,h1', 'i':'c2', 'o':'h2'},
         'd5':{'t':'d6'},
         'f5':{'n':'f6'},
         'g5':{'b':'g6'},
         'h5':{'g':'a1', 'c':'b1,d1,e1,f1,g1', 'd':'c1,h1'},
         'd6':{'u':'d7'},
         'f6':{'c':'f7'},
         'd7':{'r':'d8'},
         'f7':{'i':'f8', 'a':'d2,f2', 'o':'b2,e2', 'u':'g2'},
         'd8':{'a':'d9'},
         'f8':{'o':'f9'},
         'd9':{'g':'a1', 'c':'b1,d1,e1,f1,g1', 'd':'c1,h1'},
         'f9':{'g':'a1', 'c':'b1,d1,e1,f1,g1', 'd':'c1,h1'},
         'b3':{'t':'b4'},
         'g6':{'o':'g7'},
         'b4':{'a':'b5'},
         'g7':{'c':'g8'},
         'c4':{'a':'c5'},
         'b5':{'g':'b6'},
         'c5':{'n':'c6'},
         'g8':{'a':'g9', 'o':'b2,e2', 'u':'g2'},
         'b6':{'r':'a2', 'i':'b7'},
         'c6':{'c':'c7'},
         'g9':{'n':'f3', 's':'g10', 'l':'d3'},
         'b7':{'o':'b8'},
         'c7':{'i':'c8', 'a':'d2,f2', 'o':'b2,e2', 'u':'g2'},
         'g10':{'g':'a1', 'c':'b1,d1,e1,f1,g1', 'd':'c1,h1'},
         'b8':{'g':'a1', 'c':'b1,d1,e1,f1,g1', 'd':'c1,h1'},
         'c8':{'a':'c9'},
         'c9':{'g':'a1', 'c':'b1,d1,e1,f1,g1', 'd':'c1,h1'},
}

alfabeto = {'g','r','i','p','a','c','o','n','t','d','s','l','e','u','v','b'}

estados_finales = {'e5','a5','h5','d9','f9','g10','c9','b8'}

class AFD:

    def __init__(self,delta,alfabeto,estados_finales):
        
        self.delta = delta
        self.estado_actual='z0'
        self.alfabeto = alfabeto
        self.estados_finales = estados_finales
        self.frecuencias = dict.fromkeys(estados_finales,0)
        self.positions = { 'e5': [],
                           'a5': [],
                           'h5': [],
                           'd9': [],
                           'f9': [],
                           'g10': [],
                           'c9': [],
                           'b8': [],
        }
        
    def get_estado_actual(self):
        return self.estado_actual

    def set_estado_actual(self,estado):
        self.estado_actual = estado

    def siguiente_estado(self,caracter, counter_n, counter_w):
        
        if caracter not in self.alfabeto:
            self.set_estado_actual('z0')
        else:
            if self.delta[self.get_estado_actual()].get(caracter) is not None: #Si se encuentra esa transición
                aux = self.delta[self.get_estado_actual()].get(caracter)
                self.set_estado_actual(aux)
            
            else:
                if caracter == 'g' or caracter=='c' or caracter=='d': ##Checa si es almenos una letra de las que comienza cada cadena
                    if caracter == 'g':
                        self.set_estado_actual('a1')
                    elif caracter == 'c':
                        self.set_estado_actual('b1,d1,e1,f1,g1')
                    else:
                        self.set_estado_actual('c1,h1')

                else:
                    self.set_estado_actual('z0')

        print(caracter + ' -> ' + self.get_estado_actual())
        self.verificar_estado(counter_n, counter_w)

        return caracter + ' -> ' + self.get_estado_actual()

    def verificar_estado(self, counter_n, counter_w):

        if self.get_estado_actual() not in self.frecuencias:
            return

        else:
            aux = self.frecuencias.get(self.get_estado_actual())
            aux +=1
            self.frecuencias[self.get_estado_actual()] = aux 
            self.positions[self.get_estado_actual()].append((counter_n, counter_w))


    def printFrecuency(self):  

        file2 = open("P5\\Resultados.txt", "w", encoding="UTF-8")

        file2.write("--------RESULTS---------")
        file2.write(f"gripa = {self.frecuencias['a5']} , posiciones = {self.positions['a5']} \n")
        file2.write(f"contagio = {self.frecuencias['b8']}, posiciones = {self.positions['b8']} \n")
        file2.write(f"distancia = {self.frecuencias['c9']}, posiciones = {self.positions['c9']} \n")
        file2.write(f"calentura = {self.frecuencias['d9']}, posiciones = {self.positions['d9']} \n")
        file2.write(f"covid = {self.frecuencias['e5']}, posiciones = {self.positions['e5']} \n")
        file2.write(f"cansancio = {self.frecuencias['f9']}, posiciones = {self.positions['f9']} \n")
        file2.write(f"cubrebocas = {self.frecuencias['g10']}, posiciones = {self.positions['g10']} \n")
        file2.write(f"dolor = {self.frecuencias['h5']}, posiciones = {self.positions['h5']} \n")
       
        file2.close()

        print("--------RESULTS---------")
        print(f"gripa = {self.frecuencias['a5']} , posiciones = {self.positions['a5']} ")
        print(f"contagio = {self.frecuencias['b8']}, posiciones = {self.positions['b8']} ")
        print(f"distancia = {self.frecuencias['c9']}, posiciones = {self.positions['c9']} ")
        print(f"calentura = {self.frecuencias['d9']}, posiciones = {self.positions['d9']} ")
        print(f"covid = {self.frecuencias['e5']}, posiciones = {self.positions['e5']} ")
        print(f"cansancio = {self.frecuencias['f9']}, posiciones = {self.positions['f9']} ")
        print(f"cubrebocas = {self.frecuencias['g10']}, posiciones = {self.positions['g10']} ")
        print(f"dolor = {self.frecuencias['h5']}, posiciones = {self.positions['h5']} ")

    

if __name__ == '__main__':
    
    
    #Articulos del sitio de la ONU  https://coronavirus.onu.org.mx/
    file = ws.writeText("https://coronavirus.onu.org.mx/la-covid-19-se-estabiliza-en-las-americas-pero-los-paises-deben-permanecer-vigilantes-y-gestionar-otras-emergencias")
    automata = AFD(delta,alfabeto,estados_finales)

    file1 = open("P5\\Transciones.txt", "w", encoding="UTF-8")

    with open(file,'r',encoding='utf-8') as text:
        counter_n = 1
        for line in text:
            counter_w = 1
            for char in line:
                aux = char
                counter_w = counter_w + 1 if aux==" " else counter_w
                cadena = automata.siguiente_estado(char.lower(), counter_n, counter_w)
                file1.write(cadena + "\n")
            counter_n = counter_n + 1
    
    automata.printFrecuency()

    file1.close()
