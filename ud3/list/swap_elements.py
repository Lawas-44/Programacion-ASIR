from list_utils import read_list

# Intercambio en una sola línea mediante tuplas
def swap_elements(lista, pos1, pos2):
    lista[pos1], lista[pos2] = lista[pos2], lista[pos1]

def main():
    lista = read_list()
    pos1 = int(input("Introduce la posición del primer elemento a intercambiar: "))
    pos2 = int(input("Introduce la posición del segundo elemento a intercambiar: "))

    print(f"Lista original: {lista}")
    swap_elements(lista, pos1, pos2)
    print(f"Lista después del intercambio: {lista}")

if __name__ == "__main__":
    main()
