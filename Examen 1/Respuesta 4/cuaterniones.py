"""
Kevin Oporto ; 13-11007
Lenguajes de Programacion I
Examen I
Pregunta Nro 4

"""

import math

"""
	Se crea la clase Cuaternion, donde se le definen todas las operaciones validas para los cuaterniones
	Suma (+), producto (*), conjugada (~) y valor absoluto (.valor_absoluto())

"""
class Cuaternion:
    def __init__(self, w, x, y, z):
        self.w = w
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Cuaternion({self.w}, {self.x}, {self.y}, {self.z})"

    # Suma de cuaterniones
    def __add__(self, other):
        if isinstance(other, Cuaternion):
            return Cuaternion(
                self.w + other.w,
                self.x + other.x,
                self.y + other.y,
                self.z + other.z
            )
        elif isinstance(other, (int, float)):
            return Cuaternion(self.w + other, self.x, self.y, self.z)
        return NotImplemented

    # Producto de cuaterniones
    def __mul__(self, other):
        if isinstance(other, Cuaternion):
            w = self.w * other.w - self.x * other.x - self.y * other.y - self.z * other.z
            x = self.w * other.x + self.x * other.w + self.y * other.z - self.z * other.y
            y = self.w * other.y - self.x * other.z + self.y * other.w + self.z * other.x
            z = self.w * other.z + self.x * other.y - self.y * other.x + self.z * other.w
            return Cuaternion(w, x, y, z)
        elif isinstance(other, (int, float)):
            return Cuaternion(self.w * other, self.x * other, self.y * other, self.z * other)
        return NotImplemented

    # Conjugada del cuaternión
    def __invert__(self):
        return Cuaternion(self.w, -self.x, -self.y, -self.z)

    # Valor absoluto o norma del cuaternión
    def valor_absoluto(self):
        return math.sqrt(self.w**2 + self.x**2 + self.y**2 + self.z**2)

    # Operadores de sobrecarga, para soportar operaciones correctas con int y float
    def __radd__(self, other):
        return self.__add__(other)

    def __rmul__(self, other):
        return self.__mul__(other)
