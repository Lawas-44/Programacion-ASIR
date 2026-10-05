def is_valid_banknote(number):
    valid_banknotes = [5, 10, 20, 50, 100, 200, 500]
    if number in valid_banknotes:
        return "Is valid!"
    else:
        return "Is not valid"

def main():
    number = int(input("Introdueix un nombre enter: "))

    result = is_valid_banknote(number)
    print(result)

if __name__ == "__main__":
    main()