import os

# Comprobación de la combinación correcta
def comb_test(test, comb):
    correct = True
    for i in range(8):
        if test[i] != comb[i]:
            correct = False
    return correct

#Imprime con el formato correcto las combinaciones
def menu(comb):
    print(f"1[{comb[0]}] 5[{comb[4]}]")
    print(f"2[{comb[1]}] 6[{comb[5]}]")
    print(f"3[{comb[2]}] 7[{comb[6]}]")
    print(f"4[{comb[3]}] 8[{comb[7]}]")

def main():
    # Introducción de la clave correcta
    right_comb = str(input("Escribe la combinacion correcta (1-8) ejemplo: (1568)\n1[x] 5[x]\n2[ ] 6[x]\n3[ ] 7[ ]\n4[ ] 8[x]\n\nIntroduce la combinacion: "))
    os.system("clear")

    # Definición de variables y de la lista de combinación correcta
    test = []
    comb = []
    for i in range(8):
        comb.append(" ")
        if str(i + 1) in right_comb:
            test.append("x")
        else:
            test.append(" ")

    # Bucle de creación de nuestra combinación con depuración de errores
    n = 1
    while n != 0:
        try:
            n = int(input("Introduce un número del 1 al 8 (0 para terminar): "))
            if n == 0:
                break
            if 1 <= n <= 8:
                if comb[n - 1] == " ":
                    comb[n - 1] = "x"
                else:
                    comb[n - 1] = " "
                menu(comb)
            else:
                print("Por favor, introduce un número entre 1 y 8.")
        except ValueError:
            print("Entrada no válida. Introduce un número entero.")

    # Comprobación del resultado
    if comb_test(test, comb):
        print("\nCombinación correcta, bien hecho\n")
        menu(comb)
    else:
        print("\nError, la combinación correcta era:\n")
        menu(test)

if __name__ == "__main__":
    main()