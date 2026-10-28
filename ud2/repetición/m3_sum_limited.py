def min_multiple_three_sequence(target):
    seq = []
    total = 0
    curr = 3
    while total < target:
        seq.append(str(curr))
        total += curr
        curr += 3
    return " ".join(seq)

def main():
    target = int(input("Introdueix un nombre: "))
    output = min_multiple_three_sequence(target)
    print(output)

if __name__ == "__main__":
    main()