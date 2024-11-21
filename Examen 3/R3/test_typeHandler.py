import pytest
from typeHandler import TypeManager, main
import unittest
from unittest.mock import patch

def test_add_atomic():
	manager = TypeManager()
	manager.add_atomic("int", 4, 4)
	assert "int" in manager.types
	assert manager.types["int"] == {'type': 'atomic', 'size': 4, 'alignment': 4, 'isComposed': False}

def test_add_struct():
	manager = TypeManager()
	manager.add_atomic("int", 4, 4)
	manager.add_atomic("char", 1, 2)
	manager.add_struct("foo", ["char", "int"])
	assert "foo" in manager.types
	assert manager.types["foo"]['noPackaged']['size'] == 8
	assert manager.types["foo"]['noPackaged']['waste'] == 3
	assert manager.types["foo"]['packaged']['size'] == 5
	assert manager.types["foo"]['packaged']['waste'] == 0
	assert manager.types["foo"]['alignment'] == 2



def test_add_union():
	manager = TypeManager()
	manager.add_atomic("int", 4, 4)
	manager.add_atomic("char", 1, 2)
	manager.add_struct("foo", ["char", "int"])
	manager.add_union("baz", ["int", "foo", "char"])
	assert "baz" in manager.types
	assert manager.types["baz"]['noPackaged']['size'] == 8
	assert manager.types["baz"]['noPackaged']['waste'] == 3
	assert manager.types["baz"]['packaged']['size'] == 5
	assert manager.types["baz"]['packaged']['waste'] == 0
	assert manager.types["baz"]['alignment'] == 4

def test_describe_atomic(capsys):
	manager = TypeManager()
	manager.add_atomic("int", 4, 4)
	manager.describe("int")
	captured = capsys.readouterr()
	assert "Tipo atómico: 'int' \n - Tamaño: 4\n - Alineación: 4\n - Desperdicio: 0" in captured.out

def test_describe_struct(capsys):
	manager = TypeManager()
	manager.add_atomic("int", 4, 4)
	manager.add_atomic("char", 1, 1)
	manager.add_struct("foo", ["int", "char"])
	manager.describe("foo")
	captured = capsys.readouterr()
	assert "Tipo:  struct\nEmpaquetado: \n - Tamaño:  5 \n - Alineacion:  4 \n - Desperdicio:  0\nSin empaquetar: \n - Tamaño:  8 \n - Alineacion:  4 \n - Desperdicio:  3\nReordenado: \n Te lo debo :'(\n"  in captured.out

def test_describe_union(capsys):
	manager = TypeManager()
	manager.add_atomic("int", 4, 4)
	manager.add_atomic("char", 1, 2)
	manager.add_struct("foo", ["char", "int"])
	manager.add_union("baz", ["int", "foo", "char"])
	manager.describe("baz")
	captured = capsys.readouterr()
	assert "Tipo:  union\nEmpaquetado: \n - Tamaño:  5 \n - Alineacion:  4 \n - Desperdicio:  0\nSin empaquetar: \n - Tamaño:  8 \n - Alineacion:  4 \n - Desperdicio:  3\nReordenado: \n Te lo debo :'(\n"  in captured.out

def test_mcm():
	manager = TypeManager()
	assert manager.mcm(12, 15) == 60

def test_mcmLista():
	manager = TypeManager()
	assert manager.mcmLista([12, 15, 20]) == 60

class TestMain(unittest.TestCase):
	@patch('builtins.input', side_effect=[
		"ajnfjasn",
		"ATOMICO aafnka",
		"STRUCT afajfk",
		"UNION anflasf",
		"DESCRIBIR afaf",
		"ATOMICO int 4 4",
		"ATOMICO int 4 4"
	])
	@patch('builtins.print')
	def test_main(self, mock_print, mock_input):
		try:
			main()
		except SystemExit as e: print(f"Caught SystemExit: {e}") 
		except Exception as e: print(f"Another error occurred: {e}")
		finally:
			mock_print.assert_any_call("Error: Comando desconocido. Por favor, intente nuevamente.")
			mock_print.assert_any_call("Error: Formato incorrecto, debe ser: ATOMICO <nombre> <representación> <alineación>")
			mock_print.assert_any_call("Error: Formato incorrecto, debe ser: STRUCT <nombre> [<tipo>]")
			mock_print.assert_any_call("Error: Formato incorrecto, debe ser: UNION <nombre> [<tipo>]")
			mock_print.assert_any_call("Error: El tipo 'afaf' no está definido.")
			mock_print.assert_any_call("Error: El tipo 'int' ya está definido.")


# Ejecutar las pruebas con pytest
if __name__ == "__main__":
	unittest.main()
