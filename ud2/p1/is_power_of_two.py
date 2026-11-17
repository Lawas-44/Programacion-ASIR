def es_potencia_de_dos(num):
    while num % 2 == 0:
        num //= 2
        
    return num == 1

def main():
    num = int(input("Introduce un numero: "))

    print(es_potencia_de_dos(num))

if __name__ == "__main__":
    main()