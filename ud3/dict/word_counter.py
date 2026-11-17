# Suma 1 a la palabra o la crea con 1
def count_word(word, words):
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

# Cuenta cada palabra de la frase sin distinguir mayúsculas
def count_words(phrase):
    words = {}
    # Separa la frase en palabras por los espacios
    for word in phrase.lower().split(" "):
        count_word(word, words)

    return words


def main():
    print("Escribe una frase para contar las palabras:") 
    phrase = str(input("> "))
    
    words = count_words(phrase)

    # Ordenadas alfabéticamente, como pide el enunciado
    for word, val in sorted(words.items()):
        print(f"{word}: {val}")

if __name__ == "__main__":
    main()