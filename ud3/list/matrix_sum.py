# Lee la matriz fila a fila
def read_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"[{i}][{j}]: ")))
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(val) for val in row))

# Suma posición a posición
def matrix_sum(m1, m2):
    result = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[i])):
            row.append(m1[i][j] + m2[i][j])
        result.append(row)
    return result

def main():
    rows = int(input("Introduce el número de filas: "))
    cols = int(input("Introduce el número de columnas: "))

    print("Matriz 1:")
    m1 = read_matrix(rows, cols)
    print("Matriz 2:")
    m2 = read_matrix(rows, cols)

    print("Matriz 1:")
    print_matrix(m1)
    print("Matriz 2:")
    print_matrix(m2)
    print("Suma:")
    print_matrix(matrix_sum(m1, m2))

if __name__ == "__main__":
    main()
