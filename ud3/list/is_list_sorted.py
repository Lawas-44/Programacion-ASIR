from list_utils import read_list

def is_list_sorted(lista):
    # Comparamos cada elemento con el siguiente
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

def main():
    lista = read_list()
    if is_list_sorted(lista):
        print("La lista está ordenada ascendentemente.")
    else:
        print("La lista no está ordenada ascendentemente.")

if __name__ == "__main__":
    main()
