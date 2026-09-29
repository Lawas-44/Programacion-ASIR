import math

def calculate_circle_area(radius):
    return math.pi * radius ** 2

def main():
    radius = float(input("Introdueix el radi del cercle: "))
    area = calculate_circle_area(radius)
    print(area)

if __name__ == "__main__":
    main()