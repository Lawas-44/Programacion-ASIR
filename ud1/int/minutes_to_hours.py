# Divide los minutos en horas completas y minutos sobrantes
def convert_minutes(minutes):
    # // es la división entera y % el resto
    hours = minutes // 60
    remaining_minutes = minutes % 60

    return hours, remaining_minutes

def main():
    minutes = int(input("Introdueix els minuts: "))
    hours, remaining_minutes = convert_minutes(minutes)
    print(hours, "hores i", remaining_minutes, "minuts")

if __name__ == "__main__":
    main()