import pytest
import unittest
from unittest.mock import patch
from expressionHandler import eval_pre, eval_post, mostrar_pre, mostrar_post, main

def test_eval_pre():
	assert eval_pre(['+', '8', '9']) == 17
	assert eval_pre(['*', '12', '5']) == 60
	assert eval_pre(['/', '15', '3']) == 5
	assert eval_pre(['+', '*', '+', '3', '4', '5', '7']) == 42

def test_eval_post():
	assert eval_post(['3', '4', '+']) == 7
	assert eval_post(['2', '5', '*']) == 10
	assert eval_post(['6', '2', '/']) == 3
	assert eval_post(['8', '3', '-', '8', '4', '4', '+', '*', '+']) == 69

def test_mostrar_pre():
	assert mostrar_pre(['*', '+', '3', '4', '6']) == '((3 + 4) * 6)'
	assert mostrar_pre(['+', '/', '6', '2', '5']) == '(6 / 2 + 5)'
	assert mostrar_pre(['+', '*', '+', '3', '4', '5', '7']) == '((3 + 4) * 5 + 7)'

def test_mostrar_post():
	assert mostrar_post(['3', '4', '6', '+', '*']) == '(3 * (4 + 6))'
	assert mostrar_post(['6', '2', '5', '+', '/']) == '(6 / (2 + 5))'
	assert mostrar_post(['8', '3', '-', '8', '4', '4', '+', '*', '+']) == '(8 - 3 + 8 * (4 + 4))'


class TestMain(unittest.TestCase):
	@patch('builtins.input', side_effect=[
		"ajnfjasn",
		"EVAL anfla laflkja",
		"MOSTRAR afajfk aklfjklas",
		"alfjkkl anflasf lkafjklfam"
	])
	@patch('builtins.print')
	def test_main(self, mock_print, mock_input):
		try:
			main()
		except SystemExit as e: print(f"Caught SystemExit: {e}") 
		except Exception as e: print(f"Another error occurred: {e}")
		finally:
			mock_print.assert_any_call("Error: Argumentos insuficientes, se espera: <accion> <orden> <expresion>")
			mock_print.assert_any_call("Error: Orden desconocido, debe ser PRE o POST")
			mock_print.assert_any_call("Error: Orden desconocido, debe ser PRE o POST")
			mock_print.assert_any_call("Error: Comando no reconocido. Inténtalo de nuevo.")

if __name__ == "__main__":
	unittest.main()
