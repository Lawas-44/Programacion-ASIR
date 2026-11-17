# Devuelve el resultado y la jugada ganadora
def compare_rock_paper_scissors(player1, player2):
    match player1, player2:
        case ("rock", "rock") | ("paper", "paper") | ("scissors", "scissors"):
            return "Empat", player1

        case ("rock", "scissors") | ("scissors", "paper") | ("paper", "rock"):
            return "Guanya el jugador 1", player1

        case ("scissors", "rock") | ("paper", "scissors") | ("rock", "paper"):
            return "Guanya el jugador 2", player2

        # Jugada no reconocida
        case _:
            return "Valor introducido incorrecto (rock, paper, scissors)", None

def main():
    player1 = input("(rock/paper/scissors): ")
    player2 = input("(rock/paper/scissors): ")

    result, winner = compare_rock_paper_scissors(player1, player2)
    # winner es None si alguna jugada no era válida
    if winner is None:
        print(result)
    else:
        print(f"{result} amb {winner}")


if __name__ == "__main__":
    main()
