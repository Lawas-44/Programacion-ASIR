def full_multiply_tables(start, end):
    result = []
    for n in range(start, end + 1):
        result.append(f"=== TAULA DEL {n} ===")
        for i in range(1, 11):
            result.append(f"{n} * {i:2d} = {n * i}")
        result.append("")
    return "\n".join(result).strip()

def main():
    start = int(input("Inici: "))
    end = int(input("Final: "))
    output = full_multiply_tables(start, end)
    print(output)

if __name__ == "__main__":
    main()