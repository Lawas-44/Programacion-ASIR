# Suma múltiplos de 3 hasta alcanzar el objetivo
def min_multiple_three_sequence(target):
    seq = []
    total = 0
    curr = 3
    # Añade múltiplos hasta que la suma llegue al objetivo
    while total < target:
        seq.append(str(curr))
        total += curr
        # Siguiente múltiplo de 3
        curr += 3
    return " ".join(seq)

def main():
    target = int(input("Introdueix un nombre: "))
    output = min_multiple_three_sequence(target)
    print(output)

if __name__ == "__main__":
    main()