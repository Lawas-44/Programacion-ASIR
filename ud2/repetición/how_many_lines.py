def count_lines():
    count = 0
    while True:
        line = input()
        if line == "END":
            break
        count += 1
    return count

def main():
    output = count_lines()
    print(output)

if __name__ == "__main__":
    main()