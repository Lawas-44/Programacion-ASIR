def sum_numbers(number1, number2):
    return number1 + number2

def main():
    number1 = int(input("Introdueix el primer nombre enter: "))
    number2 = int(input("Introdueix el segon nombre enter: "))

    result = sum_numbers(number1, number2)
    print(result)

if __name__ == "__main__":
    main()