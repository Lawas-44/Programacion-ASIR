# Concatena los números de n a 1
def count_down(n):
    result = ""
    # Paso -1 para contar hacia atrás; el 0 no se incluye
    for i in range(n, 0, -1):
        result += str(i)
    return result

def main():
    n = int(input("Introdueix N: "))
    output = count_down(n)
    print(output)

if __name__ == "__main__":
    main()