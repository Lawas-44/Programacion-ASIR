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
        if letter not in string.ascii_lowercase:
            continue
        else:
            count_letter(letter, letters)

    return letters


def main():
    print("Escribe una frase para contar las palabras:") 
    phrase = str(input("> "))
    
    letters = count_letters(phrase)

    for letter, val in letters.items():
        print(f"{letter}: {val}")

if __name__ == "__main__":
    main()