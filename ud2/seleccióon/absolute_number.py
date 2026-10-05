def calculate_absolute_number(number):
    if number < 0:
        return number * -1
    else:
        return number

def main():
    number = int(input("Introdueix un nombre enter: "))

    result = calculate_absolute_number(number)
    print(result)

if __name__ == "__main__":
    main()