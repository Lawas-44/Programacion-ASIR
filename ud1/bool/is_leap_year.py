# Bisiesto: divisible entre 400, o entre 4 pero no entre 100
def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def main():
    year = int(input("Introdueix un any: "))
    result = is_leap_year(year)
    print(result)

if __name__ == "__main__":
    main()