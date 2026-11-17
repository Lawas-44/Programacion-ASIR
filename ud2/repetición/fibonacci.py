# Devuelve los n primeros términos de Fibonacci
def generate_fibonacci(n):
    # Casos especiales: ningún término o solo uno
    if n <= 0:
        return ""
    if n == 1:
        return "0"
    
    # Los dos primeros términos
    seq = [0, 1]
    # Cada término es la suma de los dos anteriores
    for i in range(2, n):
        next_val = seq[-1] + seq[-2]
        seq.append(next_val)
        
    # map(str, ...) pasa los números a texto para unirlos
    return "\n".join(map(str, seq))

def main():
    n = int(input("Introdueix N: "))
    output = generate_fibonacci(n)
    print(output)

if __name__ == "__main__":
    main()