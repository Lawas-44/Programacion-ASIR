def generate_dots(num):
    return "." * num

def main():
    num = int(input("Introdueix un nombre enter: "))
    output = generate_dots(num)
    print(output)

if __name__ == "__main__":
    main()