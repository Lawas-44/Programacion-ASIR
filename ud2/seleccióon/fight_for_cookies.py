def is_fair(cookies_amount, people_amount):
    if (cookies_amount % people_amount) == 0:
        return "Let's eat"
    else:
        return "No eat"

def main():
    cookies_amount = int(input("Introdueix el nombre de galletes: "))
    people_amount = int(input("Introdueix el nombre de persones: "))

    result = is_fair(cookies_amount, people_amount)
    print(result)

if __name__ == "__main__":
    main()