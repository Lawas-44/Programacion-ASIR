from list_utils import read_list, sum_list

def average(lista):
    return sum_list(lista) / len(lista)

def find_nearest_average(lista):
    avg = average(lista)

    # 1. Inicializamos con el primer elemento
    nearest = lista[0]

    # 2. Buscamos el que tenga menor distancia a la media
    for i in lista:
        if abs(i - avg) < abs(nearest - avg):
            nearest = i
    return nearest

def main():
    lista = read_list()
    print(f"La media es: {average(lista)}")
    nearest = find_nearest_average(lista)
    print(f"El elemento más cercano a la media es: {nearest}")

if __name__ == "__main__":
    main()
