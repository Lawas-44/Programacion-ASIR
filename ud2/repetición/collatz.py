def collatz_sequence(n):
    steps = 0
    result = [f"n0: {n}"]
    
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1
        result.append(f"n{steps}: {n}")
        
    result.append(f"Passos: {steps}")
    return "\n".join(result)

def main():
    n = int(input("Introdueix un enter positiu: "))
    output = collatz_sequence(n)
    print(output)

if __name__ == "__main__":
    main()