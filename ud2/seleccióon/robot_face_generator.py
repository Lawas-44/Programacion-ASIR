def generate_robot_face(monyo, ulls, nas, boca):
    monyo_lower = monyo.lower()
    if monyo_lower == "arrissat" or monyo_lower == "arrissats":
        linia_monyo = "@@@@@"
    elif monyo_lower == "llis":
        linia_monyo = "VVVVV"
    else:
        linia_monyo = "XXXXX"

    ulls_lower = ulls.lower()
    if ulls_lower == "aclucats":
        linia_ulls = ".-.-."
    elif ulls_lower == "redons":
        linia_ulls = ".o-o."
    else:
        linia_ulls = ".*-*."

    nas_lower = nas.lower()
    if nas_lower == "xato":
        linia_nas = "..0.."
    elif nas_lower == "arromangat":
        linia_nas = "..C.."
    else:
        linia_nas = "..V.."

    boca_lower = boca.lower()
    if boca_lower == "normal":
        linia_boca = ".===."
    elif boca_lower == "bigot":
        linia_boca = ".~~~."
    else:
        linia_boca = ".www."

    return linia_monyo + "\n" + linia_ulls + "\n" + linia_nas + "\n" + linia_boca

def main():
    monyo = input("Tipus de monyo (arrissat, llis, despentinat): ")
    ulls = input("Tipus d'ulls (aclucats, redons, estrellats): ")
    nas = input("Tipus de nas (xato, arromangat, aguilenc): ")
    boca = input("Tipus de boca (normal, bigot, dents): ")

    resultat = generate_robot_face(monyo, ulls, nas, boca)
    print(resultat)

if __name__ == "__main__":
    main()