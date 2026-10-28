def count_up(limit):
    result = ""
    for i in range(1, limit + 1):
        result += str(i)
    return result

def main():
    limit = int(input("Introdueix un nombre enter: "))
    output = count_up(limit)
    print(output)

if __name__ == "__main__":
    main()