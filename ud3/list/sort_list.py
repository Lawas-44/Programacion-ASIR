from list_utils import read_list

# Ordenación por selección: buscamos el mínimo y lo ponemos al principio
def sort_list(lista):
    # Copia para no modificar la lista original
    sorted_list = lista.copy()

    for i in range(len(sorted_list) - 1):
        min_i = i
        # Busca el mínimo en la parte sin ordenar
        for j in range(i + 1, len(sorted_list)):
            if sorted_list[j] < sorted_list[min_i]:
                min_i = j
        # Lo coloca en la posición i
        sorted_list[i], sorted_list[min_i] = sorted_list[min_i], sorted_list[i]

    return sorted_list

def main():
    lista = read_list()
    print(f"Lista original: {lista}")
    print(f"Lista ordenada: {sort_list(lista)}")

if __name__ == "__main__":
    main()
