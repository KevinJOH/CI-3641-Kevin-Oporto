#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NUM_EXECUTIONS 5
#define NUM_SIZES 5

const int sizes[NUM_SIZES] = {100, 1000, 10000, 100000, 1000000};

void initializeMatrix(int **matrix, int rows, int cols) {
	for (int i = 0; i < rows; ++i) {
		for (int j = 0; j < cols; ++j) {
			matrix[i][j] = rand() % 100;
		}
	}
}

long long sumByRow(int **matrix, int rows, int cols) {
	long long sum = 0;
	for (int i = 0; i < rows; ++i) {
		for (int j = 0; j < cols; ++j) {
			sum += matrix[i][j];
		}
	}
	return sum;
}

long long sumByCol(int **matrix, int rows, int cols) {
	long long sum = 0;
	for (int j = 0; j < cols; ++j) {
		for (int i = 0; i < rows; ++i) {
			sum += matrix[i][j];
		}
	}
	return sum;
}

double measureTime(long long (*sumFunction)(int **, int, int), int **matrix, int rows, int cols) {
	clock_t start, end;
	double cpu_time_used;

	start = clock();
	sumFunction(matrix, rows, cols);
	end = clock();

	cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
	return cpu_time_used;
}

int main() {
	srand(time(0));
	double times_sumByRow[NUM_SIZES][NUM_SIZES][NUM_EXECUTIONS];
	double times_sumByCol[NUM_SIZES][NUM_SIZES][NUM_EXECUTIONS];

	for (int r = 0; r < NUM_SIZES; ++r) {
		for (int c = 0; c < NUM_SIZES; ++c) {
			int rows = sizes[r];
			int cols = sizes[c];

			if ((rows * cols * sizeof(int)) > (1024 * 1024 * 1024)) { 
				printf("La matriz de tamaño %d x %d no cabe en memoria.\n", rows, cols);
				continue;
      }

			int **matrix = (int **) malloc(rows * sizeof(int *));
			for (int i = 0; i < rows; ++i) {
				matrix[i] = (int *) malloc(cols * sizeof(int));
			}

			initializeMatrix(matrix, rows, cols);

			for (int exec = 0; exec < NUM_EXECUTIONS; ++exec) {
				times_sumByRow[r][c][exec] = measureTime(sumByRow, matrix, rows, cols);
				times_sumByCol[r][c][exec] = measureTime(sumByCol, matrix, rows, cols);
			}

			for (int i = 0; i < rows; ++i) {
				free(matrix[i]);
			}
			free(matrix);
		}
	}

    // Guardar resultados en archivos CSV
	FILE *file_sumByRow = fopen("times_sumByRow.csv", "w");
	FILE *file_sumByCol = fopen("times_sumByCol.csv", "w");

	fprintf(file_sumByRow, "Filas,Columnas,Ejecucion 1,Ejecucion 2,Ejecucion 3,Ejecucion 4,Ejecucion 5\n");
	fprintf(file_sumByCol, "Filas,Columnas,Ejecucion 1,Ejecucion 2,Ejecucion 3,Ejecucion 4,Ejecucion 5\n");

	for (int r = 0; r < NUM_SIZES; ++r) {
		for (int c = 0; c < NUM_SIZES; ++c) {
			int rows = sizes[r];
			int cols = sizes[c];
			if ((rows * cols * sizeof(int)) > (1024 * 1024 * 1024)) {
				continue;
			}
			fprintf(file_sumByRow, "%d,%d,%f,%f,%f,%f,%f\n", rows, cols, times_sumByRow[r][c][0], times_sumByRow[r][c][1], times_sumByRow[r][c][2], times_sumByRow[r][c][3], times_sumByRow[r][c][4]);
			fprintf(file_sumByCol, "%d,%d,%f,%f,%f,%f,%f\n", rows, cols, times_sumByCol[r][c][0], times_sumByCol[r][c][1], times_sumByCol[r][c][2], times_sumByCol[r][c][3], times_sumByCol[r][c][4]);
		}
	}

	fclose(file_sumByRow);
	fclose(file_sumByCol);

	return 0;
}
