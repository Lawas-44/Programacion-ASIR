def greater_number(number1, number2):
    if number1 > number2:
        return number1
    else:
        return number2

def main():
    number1 = int(input("Introdueix un nombre enter: "))
    number2 = int(input("Introdueix un altre nombre enter: "))

    result = greater_number(number1, number2)

if __name__ == "__main__":
    main()