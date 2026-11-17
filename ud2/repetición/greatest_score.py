# Lee pares nombre/puntuación hasta END y se queda con el mejor
def find_winner():
    best_name = ""
    # -1 para que cualquier puntuación lo supere
    best_score = -1
    
    while True:
        name = input()
        if name == "END":
            break
        score = int(input())
        # Con > en caso de empate se queda el primero
        if score > best_score:
            best_score = score
            best_name = name
            
    return f"{best_name}: {best_score}"

def main():
    output = find_winner()
    print(output)

if __name__ == "__main__":
    main()