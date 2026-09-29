import math

def calculate_round_pizza_area(diameter):
    radius = diameter / 2
    return math.pi * radius ** 2

def calculate_rectangular_pizza_area(width, length):
    return width * length

def calculate_price_per_cm2(price, area):
    return price / area

def is_round_pizza_more_profitable(
        round_price, 
        round_diameter, 
        rectangular_price, 
        rectangular_width, 
        rectangular_length
):
    round_area = calculate_round_pizza_area(round_diameter)
    rectangular_area = calculate_rectangular_pizza_area(rectangular_width, rectangular_length)

    round_price_per_cm2 = calculate_price_per_cm2(round_price, round_area)

    rectangular_price_per_cm2 = calculate_price_per_cm2(rectangular_price, rectangular_area)
    
    if round_price_per_cm2 < rectangular_price_per_cm2:
        return "redona", round_price_per_cm2
    else:
        return "rectangular", rectangular_price_per_cm2


def main():
    round_price = float(input("Preu de la pizza redona: "))
    round_diameter = float(input("Diàmetre de la pizza redona: "))

    rectangular_price = float(input("Preu de la pizza rectangular: "))
    rectangular_width = float(input("Amplària de la pizza rectangular: "))
    rectangular_length = float(input("Llargària de la pizza rectangular: "))

    result, price_per_cm2 = is_round_pizza_more_profitable(
        round_price,
        round_diameter,
        rectangular_price,
        rectangular_width,
        rectangular_length)
    print(f"La pizza {result} es mes rentable: {round(price_per_cm2, 2)}")

if __name__ == "__main__":
    main()