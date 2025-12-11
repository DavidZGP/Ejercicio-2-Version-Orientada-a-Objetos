# Main.py
from mini_turtle_oo.turtle_logic import Tortuga 

t1 = Tortuga()
t2 = Tortuga()

print("Tortuga 1 movimientos:")
t1.adelante(5)
t1.abajo(2)
t1.adelante(5)
t1.abajo(2)

print("\nTortuga 2 movimientos:")   
t2.adelante(3)
t2.abajo(4)
t2.adelante(3)

t1.reiniciar()

print("Tortuga 1 despues de reiniciar:")
t1.adelante(3)
t1.abajo(3)

print("Escalón 1")
t.adelante(5)
t.abajo(2)