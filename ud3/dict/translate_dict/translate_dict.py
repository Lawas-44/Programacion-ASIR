from dict_to_import import traductor_dict

# Traduce palabra a palabra con el diccionario importado
def trasnlate_en_to_val(phrase):
    trad_phrase = []

    for word in phrase.split():
        trad_word = traductor_dict.get(word.lower(), word) # Uso get para devolver como valor por defecto la palabra en inglés

        # Respeta la mayúscula inicial de la palabra original
        if word[0].isupper():
            trad_word = trad_word[0].upper() + trad_word[1:]

        trad_phrase.append(trad_word)

    return " ".join(trad_phrase)

def main():
    print("Escribe una frase simple en inglés: ")
    phrase = input("> ")

    print(trasnlate_en_to_val(phrase))

if __name__ == "__main__":
    main()