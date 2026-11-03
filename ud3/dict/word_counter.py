def count_word(word, words):
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

def count_words(words, phrase):
    words = {}
    for word in phrase.lower().split(" "):
        count_words(word, words)

    return words


def main():
    print("Escribe una frase para contar las palabras:") 
    phrase = str(input("> "))
    
    words = count_words(phrase)

    for word, val in words.items():
        print(f"{word}: {val}")

if __name__ == "__main__":
    main()