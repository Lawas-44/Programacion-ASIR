def is_adult(age):
    return age >= 18

def main():
    age = int(input("Introdueix la teua edat: "))
    result = is_adult(age)
    print(result)

if __name__ == "__main__":
    main()