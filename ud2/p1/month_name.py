def month_name(num):
    match num:
        case 1: return "Enero"
        case 2: return "Febrero"
        case 3: return "Marzo"
        case 4: return "Abril"
        case 5: return "Mayo"
        case 6: return "Junio"
        case 7: return "Julio"
        case 8: return "Agosto"
        case 9: return "Septiembre"
        case 10: return "Octubre"
        case 11: return "Noviembre"
        case 12: return "Diciembre"
        case _: return "Valor invalido"

def main():
    num = int(input("Introduce un numero (1/12): "))
    print(month_name(num))

if __name__ == "__main__":
    main()

