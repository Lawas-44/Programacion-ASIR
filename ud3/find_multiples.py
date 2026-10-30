from list_utils import read_list

def find_multiples(num, lista):
    lista_mult = []
    for i in lista:
        if i % num == 0:
            lista_mult.append(i)
    return lista_mult

def main():
    lista = read_list()
    num = int(input("Introduce un número para encontrar sus multiplos: "))
    lista_mult = find_multiples(num, lista)
    print(lista_mult)
    
if __name__ == "__main__":
    main()