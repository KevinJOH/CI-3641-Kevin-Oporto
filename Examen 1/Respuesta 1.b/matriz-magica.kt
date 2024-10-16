/*
	Kevin Oporto ; 13-11007
	Lenguajes de Programación I
	Examen I
	Pregunta 1.b.ii) Dada una matriz cuadrada, el programa calcula si la matriz es o no mágica
*/

/*
	Para un cuadrado de tamaño nxn los numeros van desde 1 hasta n^2. La suma total es la suma de los primeros n^2 numeros
	Suma = n^2(n^2 + 1) / 2. Al agregarle las diagonales, nuestra suma mágica nos quedará = n*(n^2 + 1) /2.
	Ahora solo queda hacer la sumatoria de las filas, columnas y diagonales y si todas las sumas son iguales
	a la suma mágica, entonces la matriz será mágica, de lo contrario, no lo será.
*/
fun isMagicMatrix(matrix: Array<IntArray>): Boolean {
	val n = matrix.size
	// Calcular la constante mágica
	val magicSum = n * (n * n + 1) / 2
	// Comprobar la suma de cada fila y columna
	for (i in 0 until n) {
		var rowSum = 0
		var colSum = 0
		for (j in 0 until n) {
			rowSum += matrix[i][j]
			colSum += matrix[j][i]
		}
		if (rowSum != magicSum || colSum != magicSum) {
			return false
		}
	}

	// Comprobar la suma de las diagonales
	var diagonalSum1 = 0
	var diagonalSum2 = 0
	for (i in 0 until n) {
		diagonalSum1 += matrix[i][i]
		diagonalSum2 += matrix[i][n - 1 - i]
	}
	if (diagonalSum1 != magicSum || diagonalSum2 != magicSum) {
		return false
	}

	return true
}

/*
	Funcion principal, recibe una matriz y llama a la función isMagicMatrix
*/
fun main() {
	val matrix = arrayOf(
		intArrayOf(8, 1, 6),
		intArrayOf(3, 5, 7),
		intArrayOf(4, 9, 2)
	)

	println("LA MATRIZ \n")
	for (row in matrix) {
        for (element in row) {
            print("$element ")
        }
        println()
    }
	if (isMagicMatrix(matrix)) {
		println("\n¡¡¡ ES MÁGICA !!!")
	} else {
		println("\n¡¡¡ NO ES MÁGICA !!!")
	}
}