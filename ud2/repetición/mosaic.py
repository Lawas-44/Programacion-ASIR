# Diagonal X, debajo D y encima U
def generate_mosaic(size):
    result = []
    # i es la fila y j la columna
    for i in range(size):
        row = []
        for j in range(size):
            if i == j:
                row.append("X")
            elif i > j:
                row.append("D")
            else:
                row.append("U")
        # Cada fila se guarda como texto separado por espacios
        result.append(" ".join(row))
    return "\n".join(result)

def main():
    size = int(input("Mida: "))
    output = generate_mosaic(size)
    print(output)

if __name__ == "__main__":
    main()