# Main.py
from mini_turtle_oo.turtle_logic import Tortuga # importacion de la clase Tortuga desde el modulo turtle_logic

t1 = Tortuga() # creacion de la primera instancia de Tortuga
t2 = Tortuga() # creacion de la segunda instancia de Tortuga

print("Tortuga 1 movimientos:") # movimientos de la primera tortuga
t1.adelante(5)
t1.abajo(2)
t1.adelante(5)
t1.abajo(2)

print("\nTortuga 2 movimientos:")  # movimientos de la segunda tortuga
t2.adelante(7)
t2.abajo(4)
t2.adelante(3)

t1.reiniciar()

print("Tortuga 1 despues de reiniciar:") # movimientos de la primera tortuga despues de reiniciar
t1.adelante(5)
t1.abajo(3)

t2.reiniciar()
print("Tortuga 2 despues de reiniciar:") # movimientos de la segunda tortuga despues de reiniciar
t2.adelante(4) 
t2.abajo(2)
t2.adelante(6)

