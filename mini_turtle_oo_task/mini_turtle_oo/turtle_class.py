#Turtle_Class.py
class Turtle_Class: # creacion de la clase Turtle_Class
    def __init__(self):  #  constructor de la clase
        self.posicion_x = 0  # inicializacion de la posicion en x

def adelante(self, pasos):  # metodo para mover la tortuga hacia adelante
        print("-" * pasos + ">")
        self.posicion_x += pasos

def abajo(self, pasos):  
        for _ in range(pasos):
            print(" " * self.posicion_x + "|")
        print(" " * self.posicion_x + "v")

def reiniciar(self):  
    self.posicion_x = 0
    print("(Tortuga reiniciada)") 