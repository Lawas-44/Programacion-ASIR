# Divide entre 2 mientras sea par; si acaba en 1 era potencia de 2
def es_potencia_de_dos(num):
    # 0 y los negativos no son potencia de 2 (con 0 el bucle no acabaría)
    if num <= 0:
        return False

    # Quita todos los factores 2
    while num % 2 == 0:
        num //= 2
        
    # Si solo tenía factores 2, queda 1
    return num == 1

def main():
    num = int(input("Introduce un numero: "))

    print(es_potencia_de_dos(num))

if __name__ == "__main__":
    main()