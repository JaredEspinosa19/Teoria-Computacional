chess = { '1':{'r': ['6'], 'n':['2','5']},
          '2':{'r': ['1','3','6'], 'n':['5','7']},
          '3':{'r': ['6','8'], 'n':['2','4','7']},
          '4':{'r': ['3','8'], 'n':['7']},
          '5':{'r': ['1','6','9'], 'n':['2','10']},        
          '6':{'r': ['1','3','9','11'], 'n':['2','5','7','10']},
          '7':{'r': ['3','6','8','11'], 'n':['2','4','10','12']},
          '8':{'r': ['3','11'], 'n':['4','7','12']},
          '9':{'r': ['6','14'], 'n':['5','10','13']},
          '10':{'r': ['6','9','11','14'], 'n':['5','7','13','15']},        
          '11':{'r': ['6','8','14','16'], 'n':['7','10','12','15']},
          '12':{'r': ['8','11','16'], 'n':['7','15']},
          '13':{'r': ['9','14'], 'n':['10']},
          '14':{'r': ['9','11'], 'n':['10','13','15']},
          '15':{'r': ['11','14','16'], 'n':['10','12']},
          '16':{'r': ['11'], 'n':['12','15']}

}

estados_finales = {'16'}

alfabeto = {'r','n'}


import sys
import pydot
sys.setrecursionlimit(10**6)

class AFN:
    
    def __init__(self, delta, alfabeto, estados_finales,estado_inicial):

        self.delta = delta
        self.estados_finale = estados_finales
        self.estado_inicial = estado_inicial
        self.estado_actual = estado_inicial
        self.alfabeto = alfabeto

        self.reds = {"1","3","6","8","9","11","14","16"}
        self.blacks = {"2","4","5","7","10","12","13","15"}

        self.edges = set()

    def get_estado_actual(self):
        return self.estado_actual

    def set_estado_actual(self,estado):
        self.estado_actual = estado
    
    def getPlays(self,cadena,list,file):

       
        list.append(self.get_estado_actual())

        try:
            char = cadena[0]
        except IndexError:
            char = "F"        
        if char == "F":    
            
            file.write(",".join(list[1:])+"\n")
            
          
            for i in range(1,len(list)):
                val_1 = list[i-1]
                val_2 = list[i]
                self.edges.add((val_1, val_2))

            return

        else:
           
            for next in self.delta[self.get_estado_actual()][char]:
                self.set_estado_actual(next)
                
                self.getPlays(cadena[1:],list,file)
                list.pop()
                

    def getMoves(self,cadena,list,n_file):
        
        path = f"P4\\Moves{n_file}.txt"
        file = open(path, mode='w', encoding='utf-8')

        self.getPlays(cadena,list,file)

        file.close()
        graph = pydot.Dot("my_graph", graph_type="digraph", bgcolor="white")
        
        for i in self.edges:
            node1 = i[0]
            node2 = i[1]

            if node1 not in self.reds:
                graph.add_node(pydot.Node(node1, shape="circle",color="black"))
            else:
                graph.add_node(pydot.Node(node1, shape="circle",color="red"))

            if node2 not in self.reds:
                graph.add_node(pydot.Node(node2, shape="circle",color="black"))
            else:
                graph.add_node(pydot.Node(node2, shape="circle",color="red"))

            graph.add_edge(pydot.Edge(node1, node2, color="black"))
        
        graph.write_png(f"P4\\graph_player{n_file}.png")

        return path
