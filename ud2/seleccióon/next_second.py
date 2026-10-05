def is_valid_time(seconds: int, minutes: int, hours: int) -> bool:
    is_valid = True
    if not (0 <= seconds < 60):
        print(f"El valor {seconds} no es válido para los segundos.")
        is_valid = False
    if not (0 <= minutes < 60):
        print(f"El valor {minutes} no es válido para los minutos.")
        is_valid = False
    if not (0 <= hours < 24):
        print(f"El valor {hours} no es válido para la hora.")
        is_valid = False
    return is_valid


def next_second(seconds: int, minutes: int, hours: int):
    if not is_valid_time(seconds, minutes, hours):
        return None

    seconds += 1

    if seconds == 60:
        seconds = 0
        minutes += 1

    if minutes == 60:
        minutes = 0
        hours += 1

    if hours == 24:
        hours = 0

    return seconds, minutes, hours


def main():
    try:
        seconds = int(input("Introduce los segundos: "))
        minutes = int(input("Introduce los minutos: "))
        hours = int(input("Introduce la hora: "))
    except ValueError:
        print("Error: Debes ingresar números enteros válidos.")
        return

    result = next_second(seconds, minutes, hours)

    if result:
        sec_res, min_res, hr_res = result
        print(f"El siguiente segundo es: {hr_res:02d}:{min_res:02d}:{sec_res:02d}")


if __name__ == "__main__":
    main()