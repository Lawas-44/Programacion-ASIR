# Lee palabras hasta una línea vacía
def read_words():
    words = []
    word = input("Palabra: ")
    while word != "":
        words.append(word)
        word = input("Palabra: ")
    return words

# Agrupa en listas según la primera letra
def group_by_initial(words):
    groups = {}
    for word in words:
        initial = word[0].lower()
        if initial not in groups:
            groups[initial] = []
        groups[initial].append(word)
    return groups

def main():
    words = read_words()
    groups = group_by_initial(words)

    print("Palabras agrupadas por inicial:")
    for initial, group in groups.items():
        print(f"{initial}: {group}")

if __name__ == "__main__":
    main()
