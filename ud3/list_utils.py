def read_list():
    l = []
    num_elements = int(input("Cuantos valores tendrá la lista: "))
    for i in range(num_elements):
        l.append(int(input(f"Introduce el valor {i + 1} de la lista: ")))
    return l

def min_list(lista):
    # 1. Inicializamos con el primer elemento
    min_i = 0
    min_value = lista[0]

    # 2. Recorremos el resto de la lista
    for indice, valor in enumerate(lista):
        if valor < min_value:
            min_i = indice
    return lista[min_i]

def max_list(lista):
    # 1. Inicializamos con el primer elemento
    min_i = 0
    min_value = lista[0]

    # 2. Recorremos el resto de la lista
    for indice, valor in enumerate(lista):
        if valor > min_value:
            min_i = indice
    return lista[min_i]

def sum_list(lista):
    n = 0
    for i in lista:
        n += i
    return n

def main():
    lista = read_list()
    min_value = min_list(lista)
    print(f"El valor mínimo de la lista es: {min_value}")
    max_value = max_list(lista)
    print(f"El valor máximo de la lista es: {max_value}")
    sum_value = sum_list(lista)
    print(f"La suma de todos los elemnteos de la lista es: {sum_value}")
    

if __name__ == "__main__":
    main()