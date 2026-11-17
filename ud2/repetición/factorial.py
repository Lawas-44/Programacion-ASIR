# Multiplica de 1 a n
def calculate_factorial(n):
    # Empieza en 1, el elemento neutro de la multiplicación
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def main():
    n = int(input("Introdueix un nombre: "))
    output = calculate_factorial(n)
    print(output)

if __name__ == "__main__":
    main()