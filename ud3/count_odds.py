from list_utils import read_list

def count_odds(lista):
    odds = 0
    for i in lista:
        if i %2 == 1:
            odds += 1
    return odds

def main():
    lista = read_list()
    num_odds = count_odds(lista)
    print(f"La lista tiene {num_odds} numeros impares")

if __name__ == "__main__":
    main()