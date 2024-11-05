import time
import matplotlib.pyplot as plt

# Respuesta 4.a) F_35 recursiva
def F_35_rec(n):
	if (0<= n < 15):
		return n
	elif (n>=15):
		return F_35_rec(n-5) + F_35_rec(n-10) + F_35_rec(n-15)

# Respuesta 4.b) F_35 recursiva de cola

def F_35_rec_tail(n, ac = None):
	if ac is None:
		ac = {}
	if n in ac:
		return ac[n]

	if (0 <= n < 15):
		return n
	elif (n >= 15):
		ac[n] = F_35_rec_tail(n-5, ac) + F_35_rec_tail(n-10, ac) + F_35_rec_tail(n-15, ac)
		return ac[n]

# Respuesta 4.c) F_35 iterativa de cola

def F_35_iter_tail(n):
	ac = {}
	stack = [n]
	result = 0
    
	while stack:
		current = stack.pop()
		if current in ac:
			continue
		if 0 <= current < 15:
			ac[current] = current
		else:
			if current-5 not in ac:
				stack.append(current)
				stack.append(current-5)
			elif current-10 not in ac:
				stack.append(current)
				stack.append(current-10)
			elif current-15 not in ac:
				stack.append(current)
				stack.append(current-15)
			else:
				ac[current] = ac[current-5] + ac[current-10] + ac[current-15]

	return ac[n]


# Función para medir el tiempo de ejecución
def medir_tiempo(func, n):
    inicio = time.time()
    func(n)
    fin = time.time()
    return fin - inicio

valores_n = range(14, 101, 5)
tiempos_F = []
tiempos_F_tail = []
tiempos_F_iter = []

for n in valores_n:
    tiempos_F.append(medir_tiempo(F_35_rec, n))
    tiempos_F_tail.append(medir_tiempo(F_35_rec_tail, n))
    tiempos_F_iter.append(medir_tiempo(F_35_iter_tail, n))

plt.plot(valores_n, tiempos_F, label='F_35 (Recursiva)')
plt.plot(valores_n, tiempos_F_tail, label='F_35_tail (Rec. de Cola)')
plt.plot(valores_n, tiempos_F_iter, label='F_35_iter_tail (Iterativa)')
plt.xlabel('Valor de n')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.title('Comparación de Tiempos de Ejecución 3 funciones')
plt.legend()
plt.grid(True)
plt.savefig('Grafico_Tiempo_3funciones.png')
plt.show()


plt.plot(valores_n, tiempos_F_tail, label='F_35_tail (Rec. de Cola)')
plt.plot(valores_n, tiempos_F_iter, label='F_35_iter_tail (Iterativa)')
plt.xlabel('Valor de n')
plt.ylabel('Tiempo de Ejecución (segundos)')
plt.title('Comparación de Tiempos de Ejecución Recursiva de cola vs iterativa de cola')
plt.legend()
plt.grid(True)
plt.savefig('Grafico_Tiempo_funciones_de_cola.png')
plt.show()

