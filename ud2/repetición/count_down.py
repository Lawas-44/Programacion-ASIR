def count_down(n):
    result = ""
    for i in range(n, 0, -1):
        result += str(i)
    return result

def main():
    n = int(input("Introdueix N: "))
    output = count_down(n)
    print(output)

if __name__ == "__main__":
    main()