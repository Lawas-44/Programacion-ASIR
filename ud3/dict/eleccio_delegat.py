import time

# Avisa y devuelve False si no hay votos
def hay_votos(delegats):
    if not delegats:
        print("Aún no hay votos.")
        return False
    return True

# Claves que tienen el valor buscado
def obtener_clave(diccionario, valor_buscado):
    return [clave for clave, v in diccionario.items() if v == valor_buscado]

# Muestra el ganador; si hay empate se elige a mano
def selected(delegats):
    if not hay_votos(delegats):
        return
    
    max_v = max(delegats.values())
    ganadores = obtener_clave(delegats, max_v)
    
    if len(ganadores) == 1:
        print(f"Ganador: {ganadores[0]} ({max_v} votos)")
    else:
        print(f"Empate ({max_v} votos): {', '.join(ganadores)}")
        while True:
            elegido = input("Elige al ganador definitivo: ").strip().title()
            if elegido in ganadores:
                print(f"Delegado final: {elegido}")
                break
            print("Nombre no válido. Inténtalo de nuevo.")

def max_votes(delegats):
    if not hay_votos(delegats):
        return
    max_v = max(delegats.values())
    print("Votos máximos:")
    for i in obtener_clave(delegats, max_v):
        print(f"- {i}: {max_v}")

def count_votes(delegats):
    if not hay_votos(delegats):
        return
    print("Conteo global:")
    for p, v in delegats.items():
        print(f"- {p}: {v}")

def read_votes(votes):
    if not votes:
        print("Aún no hay votos.")
        return
    print("Lista de votos:", ", ".join(votes))

def vote(delegats, votes):
    voto = input("¿A quién votas?: ").strip().title()
    if not voto:
        print("No puedes dejarlo en blanco.")
        return
        
    votes.append(voto)
    # get evita el error si es su primer voto
    delegats[voto] = delegats.get(voto, 0) + 1
    print(f"Voto para {voto} registrado.")

def menu():
    print("\n--- MENÚ ---")
    print("1. Votar")
    print("2. Ver historial de votos")
    print("3. Ver conteo")
    print("4. Ver máximo de votos")
    print("5. Ver ganador")
    print("6. Salir")

def main():
    time.sleep(1)
    # Conteo (nombre -> votos) e historial de votos
    delegats = {}
    votes = []
    
    while True:
        menu()
        select = input("> ")
    
        match select:
            case "1": vote(delegats, votes)
            case "2": read_votes(votes)
            case "3": count_votes(delegats)
            case "4": max_votes(delegats)
            case "5": selected(delegats)
            case "6": 
                print("¡Adiós!")
                break
            case _: print("Opción no válida.")

if __name__ == "__main__":
    main()