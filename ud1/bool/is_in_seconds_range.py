def is_in_seconds_range(seconds):
    return 0 <= seconds <= 59

def main():
    seconds = int(input("Introdueix un nombre de segons: "))
    result = is_in_seconds_range(seconds)
    print(result)

if __name__ == "__main__":
    main()