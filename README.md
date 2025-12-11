# Ejercicio 2 Versión Orientada a Objetos POO 
Esta es la segunda versión del proyecto Mini-Turtle, refactorizada  a **Programación Orientada a Objetos (POO)**.

El objetivo principal de esta práctica es reemplazar las funciones globales por una clase `Tortuga` que maneje su propio estado interno sin usar `global`.

##  Estructura del Paquete

<img width="884" height="235" alt="image" src="https://github.com/user-attachments/assets/b7bd7a18-6c86-4442-b69d-b1a515ba9df3" />


## 🔧 Clase Principal

### `Tortuga`
Representa una tortuga independiente con su propia posición horizontal.

### Métodos disponibles:
- `adelante(n)`
- `abajo(n)`
- `reiniciar()`


### Ejemplo de Uso
Los usuarios importan la clase así:
```python
from mini_turtle_oo.turtle_logic import Tortuga

t = Tortuga()

t.adelante(5)
t.abajo(3)

t.reiniciar()

t.adelante(2)
t.abajo(2)
```

## Objetivo Académico
Este proyecto demuestra:
- Encapsulamiento del estado (self.posicion_x)
- Creación de múltiples objetos independientes
- Eliminación total de variables globales
- Diseño orientado a objetos aplicado a un problema simple
- Organización profesional del código en módulos y paquetes
