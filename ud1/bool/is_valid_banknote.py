def is_valid_banknote(amount):
    valid_banknotes = [5, 10, 20, 50, 100, 200, 500]
    return amount in valid_banknotes

def main():
    amount = int(input("Introdueix el valor del bitllet: "))
    result = is_valid_banknote(amount)
    print(result)

if __name__ == "__main__":
    main()