import math
from functools import reduce

class TypeManager:
	def __init__(self):
		self.types = {}

	def add_atomic(self, name, size, alignment):
		if name in self.types:
			print(f"Error: El tipo '{name}' ya está definido.")
			return
		self.types[name] = {'type': 'atomic', 'size': size, 'alignment': alignment, 'isComposed': False}

	def add_struct(self, name, fields):
		if name in self.types:
			print(f"Error: El tipo '{name}' ya está definido.")
			return
		alined = self.types[fields[0]]['alignment']
		sumPackage = 0
		sumNoPackage = 0
		espace = 0
		waste = 0
		for field in fields:
			if field not in self.types:
				print(f"Error: El tipo '{field}' no está definido.")
				return
			sumPackage += self.types[field]['size']
			if espace == 0:
				sumNoPackage += self.types[field]['size']
				espace = math.ceil(self.types[field]['size']/4) * 4
				waste += ((espace) - self.types[field]['size'])
			else:
				while (espace % self.types[field]['alignment']!=0):
					espace += 4
				sumNoPackage += self.types[field]['size']
				ocupa = (math.ceil(self.types[field]['size']/4) * 4)
				waste += ((espace) - self.types[field]['size'])
				espace += ocupa
		sumNoPackage += waste

		self.types[name] = {
			'type': 'struct', 
			'noPackaged': {'size': sumNoPackage, 'waste': waste},
			'packaged': {'size': sumPackage, 'waste': 0},
			'reordered': "Te lo debo :'(",
			'alignment': alined,
			'isComposed': True
			}

	def add_union(self, name, fields):
		if name in self.types:
			print(f"Error: El tipo '{name}' ya está definido.")
			return
		sizeUsedPackaged = []
		sizeUsedNoPackaged = [] 
		alignmentUsed = []
		for field in fields:
			if field not in self.types:
				print(f"Error: El tipo '{field}' no está definido.")
				return
			if self.types[field]['isComposed']:
				actualSizeNoPackaged = self.types[field]['noPackaged']['size']
				actualSizePackaged = self.types[field]['packaged']['size']
				sizeUsedNoPackaged.append(actualSizeNoPackaged)
				sizeUsedPackaged.append(actualSizePackaged)
			else:
				actualSize = self.types[field]['size']
				sizeUsedPackaged.append(actualSize)
				sizeUsedNoPackaged.append(actualSize)
			alignmentUsed.append(self.types[field]['alignment'])
		sizePackaged = max(sizeUsedPackaged)
		sizeNoPackaged = max(sizeUsedNoPackaged)
		alignment = self.mcmLista(alignmentUsed)

		for field in fields:
			if self.types[field]['isComposed']:
				if self.types[field]['noPackaged']['size'] == sizeNoPackaged:
					waste = self.types[field]['noPackaged']['waste']
			else:
				if self.types[field]['size'] == sizeNoPackaged:
					waste = self.types[field]['waste']

		self.types[name] = {
			'type': 'union', 
			'noPackaged': {'size': sizeNoPackaged, 'waste': waste},
			'packaged': {'size': sizePackaged, 'waste': 0},
			'reordered': "Te lo debo :'(",
			'alignment': alignment,
			'isComposed': True
			}

	def mcm(self,a,b):
		return abs(a*b) // math.gcd(a,b)

	def mcmLista(self,lista):
		return reduce(self.mcm, lista)

	def describe(self, name):
		if name not in self.types:
			print(f"Error: El tipo '{name}' no está definido.")
			return
		type_info = self.types[name]
		if type_info['type'] == 'atomic':
			size = type_info['size']
			alignment = type_info['alignment']
			print(f"Tipo atómico: '{name}' \n - Tamaño: {size}\n - Alineación: {alignment}\n - Desperdicio: 0")
		else:
			self.printComposed(type_info)

	def printComposed(self, composed):
		print("Tipo: ", composed['type'])
		print("Empaquetado: \n - Tamaño: ", composed['packaged']['size'], "\n - Alineacion: ", composed['alignment'], "\n - Desperdicio: ", composed['packaged']['waste'])
		print("Sin empaquetar: \n - Tamaño: ", composed['noPackaged']['size'], "\n - Alineacion: ", composed['alignment'], "\n - Desperdicio: ", composed['noPackaged']['waste'])
		print("Reordenado: \n", composed['reordered'])

def main():
	manager = TypeManager()
	while True:
		action = input("$> ")
		parts = action.split()
		if not parts:
			continue
		command = parts[0].upper()
		if command == 'ATOMICO':
			if len(parts) != 4:
				print("Error: Formato incorrecto, debe ser: ATOMICO <nombre> <representación> <alineación>")
				continue
			name, size, alignment = parts[1], int(parts[2]), int(parts[3])
			manager.add_atomic(name, size, alignment)
		elif command == 'STRUCT':
			if len(parts) < 3:
				print("Error: Formato incorrecto, debe ser: STRUCT <nombre> [<tipo>]")
				continue
			name = parts[1]
			fields = parts[2:]
			manager.add_struct(name, fields)
		elif command == 'UNION':
			if len(parts) < 3:
				print("Error: Formato incorrecto, debe ser: UNION <nombre> [<tipo>]")
				continue
			name = parts[1]
			fields = parts[2:]
			manager.add_union(name, fields)
		elif command == 'DESCRIBIR':
			if len(parts) != 2:
				print("Error: Formato incorrecto, debe ser: DESCRIBIR <nombre>")
				continue
			name = parts[1]
			manager.describe(name)
		elif command == 'SALIR':
			break
		else:
			print("Error: Comando desconocido. Por favor, intente nuevamente.")

if __name__ == "__main__":
	print("\n***** MANEJADOR DE TIPOS *****\n")
	main()
