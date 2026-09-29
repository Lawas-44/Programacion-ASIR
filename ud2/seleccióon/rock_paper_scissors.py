def compare_values(player1, player2):
    match player1, player2:
        case ("rock", "rock") | ("paper", "paper") | ("scissors", "scissors"):
            return "Empat", player1

        case ("rock", "scissors") | ("scissors", "paper") | ("paper", "rock"):
            return "Guanya el jugador 1", player1

        case ("scissors", "rock") | ("paper", "scissors") | ("rock", "paper"):
            return "Guanya el jugador 2", player2

        case _:
            return "Valor introducido incorrecto (rock, paper, scissors)"

def main():
    player1 = input("(rock/paper/scissors): ")
    player2 = input("(rock/paper/scissors): ")

    result, winner = compare_values(player1, player2)
    print(f"{result} amb {winner}")


if __name__ == "__main__":
    main()