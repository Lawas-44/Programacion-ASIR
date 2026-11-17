# Tres lados iguales: equilátero; dos: isósceles; ninguno: escaleno
def determine_triangle_type(a, b, c):
    if a == b == c:
        return "Equilater"
    # Basta con que dos lados sean iguales
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Escale"

def main():
    a = float(input("Introdueix la longitud del primer costat: "))
    b = float(input("Introdueix la longitud del segon costat: "))
    c = float(input("Introdueix la longitud del tercer costat: "))

    resultat = determine_triangle_type(a, b, c)
    print(f"El triangle es: {resultat}")

if __name__ == "__main__":
    main()