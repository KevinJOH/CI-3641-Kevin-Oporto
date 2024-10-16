"""
Kevin Oporto ; 13-11007
Lenguajes de Programacion I
Examen I
Pregunta Nro 3

"""
# Se crea la clase definicion para tener los programas, interpretes y traductores es diccionarios individuales
class Definicion:
	def __init__(self):
		self.programas = {}
		self.interpretes = {}
		self.traductores = {}
	# Si el programa no está definido, se guarda con clave = nombre del programa y valor = lenguaje
	def definir_programa(self, nombre, lenguaje):
		if nombre in self.programas:
			print(f"Error: El programa '{nombre}' ya está definido.")
		else:
			self.programas[nombre] = lenguaje
			print(f"Se definió el programa '{nombre}', ejecutable en '{lenguaje}'")
	# Se guarda en interpretes una clave = lenguaje con valor = lenguaje en que fue escrito
	def definir_interprete(self, lenguaje_base, lenguaje):
		self.interpretes[lenguaje] = lenguaje_base
		print(f"Se definió un intérprete para '{lenguaje}', escrito en '{lenguaje_base}'")
	# Se guarda en traductores una clave = (lenguaje origen, lenguaje destino) y valor = lenguaje en que fue escrito
	def definir_traductor(self, lenguaje_base, lenguaje_origen, lenguaje_destino):
		self.traductores[(lenguaje_origen, lenguaje_destino)] = lenguaje_base
		print(f"Se definió un traductor de '{lenguaje_origen}' hacia '{lenguaje_destino}', escrito en '{lenguaje_base}'")
	# Esta funcion pregunta si el lenguaje está escrito en LOCAL, si no, entonces llama a otra función a ver si es ejecutable
	# por diagrama T.
	def es_ejecutable(self, nombre):
		if nombre not in self.programas:
			print(f"Error: El programa '{nombre}' no está definido.")
			return False

		lenguaje = self.programas[nombre]
		if lenguaje == "LOCAL":
			print(f"Si, es posible ejecutar el programa '{nombre}'")
			return True

		if self._puede_ejecutar(lenguaje):
			print(f"Si, es posible ejecutar el programa '{nombre}'")
			return True	
		else:
			print(f"No es posible ejecutar el programa '{nombre}'")
			return False
	# Primero verifica si el lenguaje es ejecutable en LOCAL, si no, verifica si hay algún interprete para ese lenguaje
	# Si lo hay, entonces verifica si el lenguaje en que está escrito es ejecutable en maquina y asi recursivamente, hasta
	# llegar a un lenguaje que si sea ejecutable en maquina (LOCAL).
	# Si no hay ningún interpreta para esto, entonces verifica los traductores, verifica si el lenguaje de origen tiene un traductor
	# que lo traduzca a otro lenguaje, si lo hay, entonces se verifica si el lenguaje en que fue escrito es ejecutabl en maquina,
	# si lo es, entonces verifica si el lenguaje destino es ejecutable en maquina y así recursivamente, hasta llegar a un lenguaje que
	# sea ejecutable en maquina.
	# De otra manera el programa no será ejecutable.
	def _puede_ejecutar(self, lenguaje):

		if lenguaje == "LOCAL":
			return True

		if lenguaje in self.interpretes and self._puede_ejecutar(self.interpretes[lenguaje]):
			return True

		for (origen, destino), base in self.traductores.items():
			if origen == lenguaje:
				if self._puede_ejecutar(self.traductores[(origen, destino)]):
					if self._puede_ejecutar(destino):
						return True
		return False
# Funcion main, lee la entrada y llama a la función correspondiente, con los argumentos correspondientes.
def main():
	definicion = Definicion()
	while True:
		k = True
		accion = input("$> ")
		if not accion:
			k = False

		if (k == True):
			partes = accion.split()
			comando = partes[0]

			if comando == "DEFINIR":
				tipo = partes[1]
				argumentos = partes[2:]

				if tipo == "PROGRAMA":
					nombre, lenguaje = argumentos
					definicion.definir_programa(nombre, lenguaje)
				elif tipo == "INTERPRETE":
					lenguaje_base, lenguaje = argumentos
					definicion.definir_interprete(lenguaje_base, lenguaje)
				elif tipo == "TRADUCTOR":
					lenguaje_base, lenguaje_origen, lenguaje_destino = argumentos
					definicion.definir_traductor(lenguaje_base, lenguaje_origen, lenguaje_destino)
				else:
					print("Error: Tipo desconocido.")
			elif comando == "EJECUTABLE":
				nombre = partes[1]
				definicion.es_ejecutable(nombre)
			elif comando == "SALIR":
				break
			else:
				print("Error: Comando desconocido.")

if __name__ == "__main__":
	print("******* SIMULADOR DE PROGRAMAS, INTERPRETES Y TRADUCTORES *******\n")
	print("La sintáxis para realizar una acción es la siguiente: ")
	print("Definir un programa: ")
	print("DEFINIR PROGRAMA <Nombre del programa> <lenguaje>")
	print("Definir un intérprete:")
	print("DEFINIR INTERPRETE <lenguaje base> <lenguaje>")
	print("Definir un traductor:")
	print("DEFINIR TRADUCTOR <lenguaje> <lenguaje origen> <lenguaje destino>")
	print("Ejecutar un programa: ")
	print("EJECUTABLE <Nombre del programa> \n")
	print("Salir del programa: ")
	print("SALIR")
	main()
