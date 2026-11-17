# Valida cada componente y avisa de los incorrectos
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


# Suma un segundo propagando el acarreo a minutos y horas
def next_second(seconds: int, minutes: int, hours: int):
    if not is_valid_time(seconds, minutes, hours):
        return None

    seconds += 1

    # A los 60 segundos se suma un minuto
    if seconds == 60:
        seconds = 0
        minutes += 1

    # A los 60 minutos se suma una hora
    if minutes == 60:
        minutes = 0
        hours += 1

    # Pasada la medianoche vuelve a 0
    if hours == 24:
        hours = 0

    return seconds, minutes, hours


def main():
    try:
        seconds = int(input("Introduce los segundos: "))
        minutes = int(input("Introduce los minutos: "))
        hours = int(input("Introduce la hora: "))
    # int() lanza ValueError si no se introduce un número
    except ValueError:
        print("Error: Debes ingresar números enteros válidos.")
        return

    result = next_second(seconds, minutes, hours)

    # result es None si la hora no era válida
    if result:
        sec_res, min_res, hr_res = result
        # :02d rellena con ceros a la izquierda
        print(f"El siguiente segundo es: {hr_res:02d}:{min_res:02d}:{sec_res:02d}")


if __name__ == "__main__":
    main()