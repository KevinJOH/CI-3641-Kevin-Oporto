.PHONY: install start tests coverage

# Define el comando de instalación
install:
	@echo "Instalando todos los módulos necesarios..."
	pip3 install -r requirements.txt
	@echo "Instalación completada."

# Define el comando para iniciar el programa
start:
	@echo "Iniciando Type Handler..."
	python3 typeHandler.py
	@echo "Type Handler finalizado."

# Define el comando para iniciar pytest
tests:
	@echo "Iniciando pytest..."
	python3 -m pytest test_typeHandler.py

# Define el comando para mostrar la covertura
coverage:
	@echo "Mostrando covertura de codigo..."
	python3 -m coverage run -m pytest
	python3 -m coverage report
	python3 -m coverage report > coverage.txt