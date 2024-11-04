.PHONY: install start tests coverage

# Define el comando de instalación
install:
	@echo "Instalando todos los módulos necesarios..."
	pip3 install -r requirements.txt
	@echo "Instalación completada."

# Define el comando para iniciar el programa
start:
	@echo "Iniciando Expression Handler..."
	python3 expressionHandler.py
	@echo "Expression Handler finalizado."

# Define el comando para iniciar pytest
tests:
	@echo "Iniciando pytest..."
	python3 -m pytest test_exprHand.py

# Define el comando para mostrar la covertura
coverage:
	@echo "Mostrando covertura de codigo..."
	python3 -m coverage run -m pytest
	python3 -m coverage report
	python3 -m coverage report > coverage.txt