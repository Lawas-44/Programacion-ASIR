import string

# Suma 1 a la letra o la crea con 1
def count_letter(letter, letters):
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1

# Cuenta solo letras de la a a la z, en minúsculas
def count_letters(phrase):
    letters = {}

    for letter in phrase.lower():
        # Ignora espacios, signos y letras con tilde
        if letter not in string.ascii_lowercase:
            continue
        else:
            count_letter(letter, letters)

    return letters


def main():
    print("Escribe una frase para contar las letras:")
    phrase = str(input("> "))
    
    letters = count_letters(phrase)

    # Ordenadas de mayor a menor frecuencia
    for letter, val in sorted(letters.items(), key=lambda item: item[1], reverse=True):
        print(f"{letter}: {val}")

if __name__ == "__main__":
    main()