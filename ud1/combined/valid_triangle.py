def is_valid_triangle(side1, side2, side3):
    return (
        side1 + side2 > side3
        and side1 + side3 > side2
        and side2 + side3 > side1
    )

def main():
    side1 = float(input("Introdueix el primer costat: "))
    side2 = float(input("Introdueix el segon costat: "))
    side3 = float(input("Introdueix el tercer costat: "))

    result = is_valid_triangle(side1, side2, side3)
    print(result)

if __name__ == "__main__":
    main()