def generate_fibonacci(n):
    if n <= 0:
        return ""
    if n == 1:
        return "0"
    
    seq = [0, 1]
    for i in range(2, n):
        next_val = seq[-1] + seq[-2]
        seq.append(next_val)
        
    return "\n".join(map(str, seq))

def main():
    n = int(input("Introdueix N: "))
    output = generate_fibonacci(n)
    print(output)

if __name__ == "__main__":
    main()