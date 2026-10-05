def is_valid_time(seconds, minutes, hours):
    return (0 <= seconds < 60) and (0 <= minutes < 60) and (0 <= hours < 24)
    
def next_second(seconds, minutes, hours):
    if not is_valid_time(seconds, minutes, hours):
        return None

    # Avanzar un segundo
    seconds += 1

    # Manejar el acarreo (rollover) de segundos, minutos y horas
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
    seconds = int(input("Introduce los segundos: "))
    minutes = int(input("Introduce los minutos: "))
    hours = int(input("Introduce la hora: "))

    result = next_second(seconds, minutes, hours)

    if result is None:
        print("La hora introducida no es válida.")
    else:
        seconds_result, minutes_result, hours_result = result
        print(f"El siguiente segundo es: {hours_result:02d}:{minutes_result:02d}:{seconds_result:02d}")


if __name__ == "__main__":
    main()