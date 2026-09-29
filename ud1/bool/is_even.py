def is_even(number):
    return number % 2 == 0

def main():
    number = int(input("Introdueix un nombre enter: "))
    result = is_even(number)
    print(result)

if __name__ == "__main__":
    main()