from dict_to_import import traductor_dict

def trasnlate_en_to_val(phrase):
    trad_phrase = []

    for word in phrase.lower().split(" "):
        trad_word = traductor_dict.get(word, word) # Uso get para devolver como valor por defecto la palabra en inglés
        trad_phrase.append(trad_word)

    return " ".joim(trad_phrase)

def main():
    print("Escribe una frase simple en inglés: ")
    phrase = input("> ")

    print(trasnlate_en_to_val(phrase))

if __name__ == "__main__":
    main()