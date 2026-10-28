def print_multiply_table(num):
    result = []
    for i in range(1, 11):
        line = f"{num} * {i:2d} = {num * i}"
        result.append(line)
    return "\n".join(result)

def main():
    num = int(input("Introdueix un nombre enter: "))
    output = print_multiply_table(num)
    print(output)

if __name__ == "__main__":
    main()