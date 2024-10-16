"""
Se usó pytest para generar las pruebas unitarias y coverage, para hacer el reporte de cobertura.
para correr el test, es necesario instalarlos usando:
pip install pytest coverage

Luego se usaron los comandos:
pytest .\test_TDiagram.py                     ->   Realiza las pruebas unitarias
coverage run -m pytest .\test_TDiagram.py     ->   Realiza el reporte de cobertura
coverage report > coverage.txt                -> Devuelve el reporte en un archivo coverage.txt

"""
import pytest
import unittest
from unittest.mock import patch
from T_Diagram import Definicion, main

def test_definir_programa():
	definicion = Definicion()
	definicion.definir_programa("Qloq", "Python")
	assert "Qloq" in definicion.programas
	assert definicion.programas["Qloq"] == "Python"

	definicion.definir_programa("XD", "C")
	assert "XD" in definicion.programas
	assert definicion.programas["XD"] == "C"

def test_definir_interprete():
	definicion = Definicion()
	definicion.definir_interprete("Python", "Java")
	assert "Java" in definicion.interpretes
	assert definicion.interpretes["Java"] == "Python"

	definicion.definir_interprete("wtf", "Java")
	assert "Java" in definicion.interpretes
	assert definicion.interpretes["Java"] == "wtf"

	definicion.definir_interprete("C", "Python")
	assert "Python" in definicion.interpretes
	assert definicion.interpretes["Python"] == "C"

def test_definir_traductor():
	definicion = Definicion()
	definicion.definir_traductor("Python", "Java", "C")
	assert ("Java", "C") in definicion.traductores
	assert definicion.traductores[("Java", "C")] == "Python"

	definicion.definir_traductor("C", "wtf", "Java")
	assert ("wtf", "Java") in definicion.traductores
	assert definicion.traductores[("wtf", "Java")] == "C"

def test_es_ejecutable():
	definicion = Definicion()
	definicion.definir_programa("Qloq", "Python")
	definicion.definir_interprete("LOCAL", "Python")
	assert definicion.es_ejecutable("Qloq")
    
	definicion.definir_programa("Yayaju", "Java")
	definicion.definir_traductor("C", "Java", "Python")
	assert definicion.es_ejecutable("Yayaju") == False

	definicion.definir_interprete("LOCAL", "C")
	assert definicion.es_ejecutable("Yayaju")

	definicion.definir_programa("Yalo", "wtf")
	assert definicion.es_ejecutable("Yalo") == False

	definicion.definir_traductor("Java", "Python", "wtf")
	assert definicion.es_ejecutable("Yalo") == False

	definicion.definir_traductor("Java", "wtf", "Python")
	assert definicion.es_ejecutable("Yalo")

	definicion.definir_programa("Dorito", "ASGARD")
	assert definicion.es_ejecutable("Dorito") == False

	definicion.definir_traductor("Paskal", "ASGARD", "Cobol")
	assert definicion.es_ejecutable("Dorito") == False

	definicion.definir_traductor("wtf", "Paskal", "Python")
	assert definicion.es_ejecutable("Dorito") == False

	definicion.definir_traductor("Python", "Cobol", "Haskell")
	assert definicion.es_ejecutable("Dorito") == False

	definicion.definir_interprete("LOCAL", "Haskell")
	assert definicion.es_ejecutable("Dorito")

def test_puede_ejecutar():
	definicion = Definicion()
	assert definicion._puede_ejecutar("Python") == False

	definicion.definir_interprete("LOCAL", "Python")
	assert definicion._puede_ejecutar("Python")

	assert definicion._puede_ejecutar("ASGARD") == False
	definicion.definir_traductor("C", "ASGARD", "Java")
	assert definicion._puede_ejecutar("ASGARD") == False
	definicion.definir_traductor("Python", "C", "Python")
	assert definicion._puede_ejecutar("ASGARD") == False
	definicion.definir_traductor("C", "Java", "Paskal")
	assert definicion._puede_ejecutar("ASGARD") == False
	definicion.definir_interprete("LOCAL", "Paskal")
	assert definicion._puede_ejecutar("ASGARD")


@patch('builtins.input', side_effect=[
	"EJECUTABLE Qloq",
	"DEFINIR PROGRAMA Qloq Java",
	"DEFINIR INTERPRETE LOCAL Python",
	"EJECUTABLE Qloq",
	"DEFINIR TRADUCTOR Python Java LOCAL",
	"DEFINIR cualquier cosa",
	"EJECUTABLE Qloq",
	"Cualquier cosa",
	"DEFINIR PROGRAMA Qloq Java",
	"SALIR"
])
def test_main(mock_input):
	with patch('builtins.print') as mock_print:
		main()
		mock_print.assert_any_call("Error: El programa 'Qloq' no está definido.")
		mock_print.assert_any_call("Se definió el programa 'Qloq', ejecutable en 'Java'")
		mock_print.assert_any_call("Se definió un intérprete para 'Python', escrito en 'LOCAL'")
		mock_print.assert_any_call("No es posible ejecutar el programa 'Qloq'")
		mock_print.assert_any_call("Se definió un traductor de 'Java' hacia 'LOCAL', escrito en 'Python'")
		mock_print.assert_any_call("Error: Tipo desconocido.")
		mock_print.assert_any_call("Si, es posible ejecutar el programa 'Qloq'")
		mock_print.assert_any_call("Error: Comando desconocido.")
		mock_print.assert_any_call("Error: El programa 'Qloq' ya está definido.")

if __name__ == '__main__':
	pytest.main()

