from matrix_sum import read_matrix, print_matrix

def is_matrix_symmetric(matrix):
    # Una matriz es simétrica si [i][j] == [j][i]
    for i in range(len(matrix)):
        # Basta con revisar lo que hay encima de la diagonal
        for j in range(i + 1, len(matrix)):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

def main():
    n = int(input("Introduce el número de filas/columnas: "))
    matrix = read_matrix(n, n)

    print("Matriz:")
    print_matrix(matrix)

    if is_matrix_symmetric(matrix):
        print("La matriz es simétrica.")
    else:
        print("La matriz no es simétrica.")

if __name__ == "__main__":
    main()
