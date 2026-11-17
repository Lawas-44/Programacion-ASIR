from list_utils import read_list, reverse, equals

# Capicúa si coincide con su inversa
def cap_i_cua(lista):
    return equals(lista, reverse(lista))

def main():
    lista = read_list()
    if cap_i_cua(lista):
        print("La lista es capicúa.")
    else:
        print("La lista no es capicúa.")

if __name__ == "__main__":
    main()
