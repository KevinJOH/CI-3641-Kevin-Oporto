"""
Se usó pytest para generar las pruebas unitarias y coverage, para hacer el reporte de cobertura.
para correr el test, es necesario instalarlos usando:
pip install pytest coverage

Luego se usaron los comandos:
pytest .\test_cuaterniones.py                     ->   Realiza las pruebas unitarias
coverage run -m pytest .\test_cuaterniones.py     ->   Realiza el reporte de cobertura
coverage report > coverage.txt                -> Devuelve el reporte en un archivo coverage.txt

"""

import pytest
import math
from cuaterniones import Cuaternion

def test_inicializacion_cuaternion():
	a = Cuaternion(7, 11, 30, 12)
	assert a.w == 7
	assert a.x == 11
	assert a.y == 30
	assert a.z == 12

def test_suma_cuaterniones():
	a = Cuaternion(1, 2, 3, 4)
	b = Cuaternion(5, 6, 7, 8)
	res = a + b
	assert res.w == 6
	assert res.x == 8
	assert res.y == 10
	assert res.z == 12

def test_producto_cuaterniones():
	a = Cuaternion(1, 2, 3, 4)
	b = Cuaternion(5, 6, 7, 8)
	res = a * b
	assert res.w == -60
	assert res.x == 12
	assert res.y == 30
	assert res.z == 24

def test_conjugado_cuaterniones():
	a = Cuaternion(1, 2, 3, 4)
	res = ~a
	assert res.w == 1
	assert res.x == -2
	assert res.y == -3
	assert res.z == -4

def test_valor_absoluto_cuaterniones():
	a = Cuaternion(1, 2, 3, 4)
	res = a.valor_absoluto()
	assert res == math.sqrt(30)

def test_suma_con_escalar():
	a = Cuaternion(1, 2, 3, 4)
	res = a + 3
	assert res.w == 4
	assert res.x == 2
	assert res.y == 3
	assert res.z == 4

def test_producto_con_escalar():
	a = Cuaternion(1, 2, 3, 4)
	res = a * 3
	assert res.w == 3
	assert res.x == 6
	assert res.y == 9
	assert res.z == 12

def test_operaciones_combinadas():
	a = Cuaternion(1, 2, 3, 4)
	b = Cuaternion(5, 6, 7, 8)
	c = Cuaternion(9, 10, 11, 12)
	res = (a * b) + c
	assert res.w == -51
	assert res.x == 22
	assert res.y == 41
	assert res.z == 36

	res = (b + b) * (c + ~a)
	assert res.w == -236
	assert res.x == 184
	assert res.y == 252
	assert res.z == 224

	res = (c * b).valor_absoluto()
	assert res == math.sqrt(77604)

	res = a * 3 + 7
	assert res.w == 10
	assert res.x == 6
	assert res.y == 9
	assert res.z == 12

	res = (b + b) * c.valor_absoluto()
	absolute = math.sqrt(446)
	assert res.w == 10 * absolute
	assert res.x == 12 * absolute
	assert res.y == 14 * absolute
	assert res.z == 16 * absolute


if __name__ == "__main__":
	pytest.main()
