def play_adventure():
    print("Et despertes a una illa de nit. L'ultim que recordes es ofegar-te.")
    print("Que vols fer?")
    print("1. Espere")
    print("2. Vaig a cercar menjar")
    
    opcio1 = input("Opcio (1/2): ")
    
    if opcio1 == "1":
        print("\nS'ha fet de dia. Tens molta fam.")
        print("Que vols fer?")
        print("1. Espere")
        print("2. Vaig a cercar menjar")
        
        opcio2 = input("Opcio (1/2): ")
        if opcio2 == "1":
            return "Has mort de fam."
        elif opcio2 == "2":
            print("\nHi ha una palmera amb cocos.")
            print("Que vols fer?")
            print("1. No hi puge, es perillos")
            print("2. Vaig a pujar!")
            
            opcio3 = input("Opcio (1/2): ")
            if opcio3 == "1":
                return "Has mort de fam."
            elif opcio3 == "2":
                return "Des de dalt de la palmera veus un vaixell. Estas salvat!"
            else:
                return "Opcio no valida."
        else:
            return "Opcio no valida."

    elif opcio1 == "2":
        return "Es de nit, no veus res. T'esperes igualment."
    else:
        return "Opcio no valida."

def main():
    resultat = play_adventure()
    print("\n" + resultat)

if __name__ == "__main__":
    main()