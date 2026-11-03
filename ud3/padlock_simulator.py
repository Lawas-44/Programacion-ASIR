import os


# Comprobación de la combinación correcta usando listas de booleanos
def comb_test(test, comb):
  return test == comb


# Imprime con el formato correcto traduciendo los booleanos
def menu(comb):
  # Función auxiliar para convertir booleanos
  translate = lambda val: "x" if val else " "

  print(f"1[{translate(comb[0])}] 5[{translate(comb[4])}]")
  print(f"2[{translate(comb[1])}] 6[{translate(comb[5])}]")
  print(f"3[{translate(comb[2])}] 7[{translate(comb[6])}]")
  print(f"4[{translate(comb[3])}] 8[{translate(comb[7])}]")


def main():
  # Introducción de la clave correcta
  right_comb = str(
      input(
          "Escribe la combinacion correcta (1-8) ejemplo: (1568)\n1[x]"
          " 5[x]\n2[ ] 6[x]\n3[ ] 7[ ]\n4[ ] 8[x]\n\nIntroduce la"
          " combinacion: "
      )
  )
  os.system("clear")

  # Definición de variables como listas de booleanos (True / False)
  test = [False] * 8
  comb = [False] * 8

  for i in range(8):
    if str(i + 1) in right_comb:
      test[i] = True

  # Bucle de creación de nuestra combinación con depuración de errores
  n = 1
  while n != 0:
    try:
      n = int(input("Introduce un número del 1 al 8 (0 para terminar): "))
      if n == 0:
        break
      if 1 <= n <= 8:
        # Alterna el valor booleano (True pasa a False y viceversa)
        comb[n - 1] = not comb[n - 1]
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