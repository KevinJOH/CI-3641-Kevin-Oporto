"""
Kevin Oporto 13-11007
CI-3641 Lenguajes de Programacion
Examen 2 - Respuesta 2
"""
def eval_pre(expr):
	stack = []
	for token in reversed(expr):
		if token.isdigit():
			stack.append(int(token))
		else:
			a = stack.pop()
			b = stack.pop()
			if token == '+':
				stack.append(a + b)
			elif token == '-':
				stack.append(a - b)
			elif token == '*':
				stack.append(a * b)
			elif token == '/':
				stack.append(a // b)
	return stack[0]

def eval_post(expr):
	stack = []
	for token in expr:
		if token.isdigit():
			stack.append(int(token))
		else:
			b = stack.pop()
			a = stack.pop()
			if token == '+':
				stack.append(a + b)
			elif token == '-':
				stack.append(a - b)
			elif token == '*':
				stack.append(a * b)
			elif token == '/':
				stack.append(a // b)
	return stack[0]

def mostrar_pre(expr):
	stack = []
	for token in reversed(expr):
		if token.isdigit():
			stack.append(token)
		else:
			a = stack.pop()
			b = stack.pop()
			if token in '+-':
				if a.startswith('(') and a.endswith(')'):
					a = a[1:-1]
				if b.startswith('(') and b.endswith(')'):
					b = b[1:-1]
			stack.append(f'({a} {token} {b})')
	return stack[0]

def mostrar_post(expr):
	stack = []
	for token in expr:
		if token.isdigit():
			stack.append(token)
		else:
			b = stack.pop()
			a = stack.pop()
			if token in '+-':
				if a.startswith('(') and a.endswith(')'):
					a = a[1:-1]
				if b.startswith('(') and b.endswith(')'):
					b = b[1:-1]
			stack.append(f'({a} {token} {b})')
	return stack[0]

def main():
	while True:
		k = True
		action = input("$> ")
		if not action:
			k = False
		
		if action == 'SALIR':
			break

		if (k == True):
			parts = action.split()
			command = parts[0]
			if len(parts) < 3:
				print("Error: Argumentos insuficientes, se espera: <accion> <orden> <expresion>")
				continue
			order = parts[1]
			expr = parts[2:]	
			if command == 'EVAL':
				if order == 'PRE':
					print(f"Resultado: {eval_pre(expr)}")
				elif order == 'POST':
					print(f"Resultado: {eval_post(expr)}")
				else:
					print("Error: Orden desconocido, debe ser PRE o POST")
			elif command == 'MOSTRAR':
				if order == 'PRE':
					print(f"Expresión en orden infijo: {mostrar_pre(expr)}")
				elif order == 'POST':
					print(f"Expresión en orden infijo: {mostrar_post(expr)}")
				else:
					print("Error: Orden desconocido, debe ser PRE o POST")
			else:
				print("Error: Comando no reconocido. Inténtalo de nuevo.")

if __name__ == "__main__":
	print("\n***** MANEJADOR DE EXPRESIONES PRE Y POST ORDEN *****\n")
	print("La sintáxis para realizar una acción es la siguiente: ")
	print("Evaluar una expresion: ")
	print("EVAL <orden (PRE ó POST)> <expresion>")
	print("Mostrar orden in-fijo de la expresion: ")
	print("MOSTRAR <orden (PRE ó POST)> <expresion>")
	print("Salir del programa: ")
	print("SALIR\n")
	main()
