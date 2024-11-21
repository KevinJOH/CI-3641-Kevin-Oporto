import csv
import matplotlib.pyplot as plt
import os

def readCsv(file_name):
	results = {}
	with open(file_name, 'r') as file:
		reader = csv.reader(file)
		headers = next(reader)
		for row in reader:
			rows = int(row[0])
			cols = int(row[1])
			times = [float(time) for time in row[2:]]
			results[(rows, cols)] = times
	return results

def plotComparison(times_sumByRow, times_sumByCol):
	for size in times_sumByRow.keys():
		if size not in times_sumByCol:
			continue
        
		sumByRow_times = times_sumByRow[size]
		sumByCol_times = times_sumByCol[size]

		plt.figure(figsize=(10, 6))
		plt.plot(range(1, len(sumByRow_times) + 1), sumByRow_times, label='Por filas', marker='o')
		plt.plot(range(1, len(sumByCol_times) + 1), sumByCol_times, label='Por columnas', marker='x')
		plt.xlabel('Ejecuciones')
		plt.ylabel('Tiempo (segundos)')
		plt.title(f'Comparación de tiempos para tamaño {size[0]}x{size[1]}')
		plt.legend()
		plt.grid(True)
		plt.savefig(f'Graficos/comparison_{size[0]}x{size[1]}.png')
		plt.show()
		plt.close()

def main():
	times_sumByRow = readCsv("times_sumByRow.csv")
	times_sumByCol = readCsv("times_sumByCol.csv")
	plotComparison(times_sumByRow, times_sumByCol)

if __name__ == "__main__":
	main()
