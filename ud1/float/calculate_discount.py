def calculate_final_price(price, discount):
    discount_amount = price * discount / 100
    return price - discount_amount

def main():
    price = float(input("Introdueix el preu del producte: "))
    discount = float(input("Introdueix el percentatge de descompte: "))
    final_price = calculate_final_price(price, discount)
    print(final_price)

if __name__ == "__main__":
    main()