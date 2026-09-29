def is_adult(age):
    if age > 18:
        return "Eres major d'edat!"
    else:
        return "No eres major d'edat!"

def main():
    age = int(input("Introdueix la teua edat: "))

    result = is_adult(age)

if __name__ == "__main__":
    main()