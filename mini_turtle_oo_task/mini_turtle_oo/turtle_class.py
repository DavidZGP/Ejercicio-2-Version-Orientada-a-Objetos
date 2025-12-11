class Turtle_Class:
    def __init__(self):
        self.posicion_x = 0

def adelante(self, pasos):
        print("-" * pasos + ">")
        self.posicion_x += pasos

def abajo(self, pasos):
        for _ in range(pasos):
            print(" " * self.posicion_x + "|")
        print(" " * self.posicion_x + "v")