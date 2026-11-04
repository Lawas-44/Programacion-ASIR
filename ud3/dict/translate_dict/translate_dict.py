from dict_to_import import traductor_dict

def trasnlate_en_to_val(phrase):
    trad_phrase = ""

    for word in phrase.split(" "):
        trad_word = traductor_dict.get(word, word)
        trad_phrase += trad_word + " "

    return trad_phrase.strip()

def main():
    print("Escribe una frase simple en inglés: ")
    phrase = input("> ").lower()

    print(trasnlate_en_to_val(phrase))

if __name__ == "__main__":
    main()