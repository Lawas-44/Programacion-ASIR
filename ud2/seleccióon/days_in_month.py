def get_days_per_month(mark):
    match mark:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12:
            return 31
        case 4 | 6 | 11:
            return 30
        case 2:
            return 28
        case _:
            return -1
        
def main():
    month = int(input("Introduce el número del mes: "))
    result = get_days_per_month(month)
    if result == -1:
        print("Mes inválido")
    else:
        print(result)

if __name__ == "__main__":
    main()