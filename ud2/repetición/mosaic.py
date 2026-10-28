def generate_mosaic(size):
    result = []
    for i in range(size):
        row = []
        for j in range(size):
            if i == j:
                row.append("X")
            elif i > j:
                row.append("D")
            else:
                row.append("U")
        result.append(" ".join(row))
    return "\n".join(result)

def main():
    size = int(input("Mida: "))
    output = generate_mosaic(size)
    print(output)

if __name__ == "__main__":
    main()