def mark_result(mark):
    match mark:
        case (0, 1, 2, 3, 4):
            return "Suspés"
        case 5:
            return "Suficient"
        case 6:
            return "Bé"
        case (7, 8):
            return "Notable"
        case (9, 10):
            return "Excel-lent"

def main():
    mark = int(input("Introduce tu nota: "))
    result = mark_result(mark)

    print(result)

if __name__ == "__main__":
    main()