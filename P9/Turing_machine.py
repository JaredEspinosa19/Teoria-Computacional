DELTA = { "q0" : {"0": {"n": "q1", "c": "X", "p":1}, "Y": {"n": "q3", "c": "Y", "p":1}},
          "q1" : {"0": {"n": "q1", "c": "0", "p":1}, "1": {"n": "q2", "c": "Y", "p":-1}, "Y": {"n": "q1", "c": "Y", "p":1}},
          "q2" : {"0": {"n": "q2", "c": "0", "p":-1}, "X": {"n": "q0", "c": "X", "p":1}, "Y": {"n": "q2", "c": "Y", "p":-1}},
          "q3" : {"Y": {"n": "q3", "c": "Y", "p":1}, "B": {"n": "q4", "c": "B", "p":1}},
}

class TM(object):

    def __init__(self):
        
        self.delta = DELTA
        self.estado_actual='q0'
        
    def get_estado_actual(self):
        return self.estado_actual

    def set_estado_actual(self,estado):
        self.estado_actual = estado

    def siguiente_estado(self,caracter):
        
        #Checar si esa transición existe
        if self.get_estado_actual() not in self.delta.keys(): 
            return caracter, 0, False
        else:
            if self.delta[self.get_estado_actual()].get(caracter) is None:
                return caracter, 0, False

            else: #Si existe
                new_state = self.delta[self.get_estado_actual()][caracter]["n"]
                new_char = self.delta[self.get_estado_actual()][caracter]["c"]
                index = self.delta[self.get_estado_actual()][caracter]["p"]
                
                self.set_estado_actual(new_state)
                
                return new_char, index, True

