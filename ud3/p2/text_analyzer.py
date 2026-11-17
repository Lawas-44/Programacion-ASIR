# Caracteres sin espacios: suma de longitudes de las palabras
def count_chars(words):
    total = 0
    for word in words:
        total += len(word)
    return total

def longest_word(words):
    longest = words[0]
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

def shortest_word(words):
    shortest = words[0]
    for word in words:
        if len(word) < len(shortest):
            shortest = word
    return shortest

# Apariciones de cada palabra
def count_words(words):
    count = {}
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

def main():
    text = input("> ")
    words = text.split()

    if not words:
        print("No has escrito ningún texto.")
        return

    count = count_words(words)

    print(f"Número de palabras: {len(words)}")
    print(f"Número de caracteres: {count_chars(words)}")
    print(f"Palabra más larga: {longest_word(words)}")
    print(f"Palabra más corta: {shortest_word(words)}")
    print(f"Número de palabras únicas: {len(count)}")
    print("Apariciones de cada palabra:")
    for word, val in count.items():
        print(f"- {word}: {val}")

if __name__ == "__main__":
    main()
