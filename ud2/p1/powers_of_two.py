def power(num):
    for i in range(num + 1):
        print(f"{2}^{i} = {2**i}")

def main():
    num = int(input("Introduce un numero: "))

    power(num)

if __name__ == "__main__":
    main()