def check_isbn(isbn):
    # Quitamos los guiones por si el código los lleva
    isbn = isbn.replace("-", "")

    if len(isbn) != 13 or not isbn.isdigit():
        return False
    if isbn[:3] not in ["978", "979"]:
        return False

    # Los 12 primeros dígitos se multiplican alternando por 1 y por 3
    total = 0
    for i in range(12):
        if i % 2 == 0:
            total += int(isbn[i])
        else:
            total += int(isbn[i]) * 3

    control = (10 - total % 10) % 10
    return control == int(isbn[12])

def main():
    isbn = input("Introduce un código ISBN-13: ")
    if check_isbn(isbn):
        print("El código ISBN es válido.")
    else:
        print("El código ISBN no es válido.")

if __name__ == "__main__":
    main()
