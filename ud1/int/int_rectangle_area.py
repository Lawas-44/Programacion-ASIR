def calculate_rectangle_area(base, height):
    return base * height

def main():
    base = int(input("Introdueix la base del rectangle: "))
    height = int(input("Introdueix l'altura del rectangle: "))

    area = calculate_rectangle_area(base, height)
    print(area)

if __name__ == "__main__":
    main()