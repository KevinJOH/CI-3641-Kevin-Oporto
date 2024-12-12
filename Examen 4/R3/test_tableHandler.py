import pytest
from tableHandler import ClassTable, main
import unittest
from unittest.mock import patch

class ClassTableTest(unittest.TestCase):
    def setUp(self):
        self.class_table = ClassTable()

    def test_add_class_without_superclass(self):
        self.class_table.addClass("A", ["f", "g"])
        self.assertIn("A", self.class_table.classes)
        self.assertListEqual(self.class_table.classes["A"]["methods"], ["f", "g"])
        self.assertIsNone(self.class_table.classes["A"]["superclass"])

    def test_add_class_with_superclass(self):
        self.class_table.addClass("A", ["f", "g"])
        self.class_table.addClass("B", ["f", "h"], "A")
        self.assertIn("B", self.class_table.classes)
        self.assertListEqual(self.class_table.classes["B"]["methods"], ["f", "h"])
        self.assertEqual(self.class_table.classes["B"]["superclass"], "A")

    def test_detect_cycle(self):
        self.class_table.addClass("A", ["f"])
        self.class_table.addClass("B", ["g"], "A")
        self.class_table.addClass("C", ["h"], "B")
        self.assertFalse(self.class_table.detectCycle("C", "B"))

    def test_describe_class(self):
        self.class_table.addClass("A", ["f", "g"])
        self.class_table.addClass("B", ["f", "h"], "A")
        expected_output = {
            "f": "B :: f",
            "g": "A :: g",
            "h": "B :: h"
        }
        actual_output = self.class_table.buildTable("B")
        self.assertDictEqual(expected_output, actual_output)

    def test_add_duplicate_class(self):
        self.class_table.addClass("A", ["f"])
        self.class_table.addClass("A", ["g"])
        self.assertEqual(len(self.class_table.classes), 1)
        self.assertListEqual(self.class_table.classes["A"]["methods"], ["f"])

class TestMain(unittest.TestCase):
	@patch('builtins.input', side_effect=[
		"ajnfjasn",
		"CLASS A : B f g",
		"CLASS B f f",
		"CLASS A f g",
		"CLASS A b y",
		"DESCRIBIR C"
	])
	@patch('builtins.print')
	def test_main(self, mock_print, mock_input):
		try:
			main()
		except SystemExit as e: print(f"Caught SystemExit: {e}") 
		except Exception as e: print(f"Another error occurred: {e}")
		finally:
			mock_print.assert_any_call("Error: Acción no reconocida.")
			mock_print.assert_any_call("Error: La clase base B no existe.")
			mock_print.assert_any_call("Error: Hay definiciones repetidas en la lista de nombres de métodos.")
			mock_print.assert_any_call("Error: La clase A ya existe.")
			mock_print.assert_any_call("Error: La clase C no existe.")

if __name__ == "__main__":
    unittest.main()
