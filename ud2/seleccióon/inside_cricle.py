import math

def is_inside_circle(x, y, a, b, r):
    distance = math.sqrt((x - a) ** 2 + (y - b) ** 2)
    return distance <= r

def main():
    x = float(input("Introdueix la coordenada x del punt: "))
    y = float(input("Introdueix la coordenada y del punt: "))
    a = float(input("Introdueix la coordenada a del centre: "))
    b = float(input("Introdueix la coordenada b del centre: "))
    r = float(input("Introdueix el radi r de la circumferencia: "))

    if is_inside_circle(x, y, a, b, r):
        print("El punt esta dins del cercle.")
    else:
        print("El punt esta fora del cercle.")

if __name__ == "__main__":
    main()