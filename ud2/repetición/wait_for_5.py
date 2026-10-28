def wait_for_five():
    while True:
        val = int(input("Introdueix un enter: "))
        if val == 5:
            return "5 trobat!"

def main():
    output = wait_for_five()
    print(output)

if __name__ == "__main__":
    main()