# Números entre start y end, sin incluirlos
def count_between(start, end):
    result = ""
    # start + 1 excluye el inicio; range ya excluye el final
    for i in range(start + 1, end):
        result += str(i)
    return result

def main():
    start = int(input("Inici: "))
    end = int(input("Final: "))
    output = count_between(start, end)
    print(output)

if __name__ == "__main__":
    main()