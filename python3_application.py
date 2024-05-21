def vstupne_parametre():
    dochodkovy_vek = 86
    meno = input('Meno:')
    priezvisko = input("Priezvisko:")
    while True:  # Kontrola datoveho typu parametru vek
        vek = input("Vek:")
        try:
            vek = int(vek)
            if vek >= 0:
                break
            else:
                print("Vek musi byt kladne cislo!")
        except ValueError:
            print("Vek musi byt cele cislo!")
    while True:  # Kontrola datoveho typu parametru pocet_rokov
        pocet_rokov = input('Pocet rokov:')
        try:
            pocet_rokov = int(pocet_rokov)
            if pocet_rokov >= 0:
                break
            else:
                print("Pocet rokov musi byt kladne cislo!")
        except ValueError:
            print("Pocet rokov musi byt cele cislo!")
    return meno, priezvisko, vek, dochodkovy_vek, pocet_rokov

def vystupne_parametre(meno, priezvisko, vek, dochodkovy_vek, pocet_rokov):
    sucet_rokov = vek + pocet_rokov
    if sucet_rokov > 85:  # Kontrola dochodkoveho veku
        return "v dochodkovom veku."
    elif sucet_rokov < 19:  # Kontrola veku do 18
        return "mat menej ako 18 rokov."
    else:
        return "v produktivnom veku."

meno, priezvisko, vek, dochodkovy_vek, pocet_rokov = vstupne_parametre()
vystup = vystupne_parametre(meno, priezvisko, vek, dochodkovy_vek, pocet_rokov)

def stylistika(cislo):
    if cislo == 1:
        return "rok"
    elif 1 < cislo < 5:
        return "roky"
    else:
        return "rokov"

slovo1 = stylistika(vek)
slovo2 = stylistika(pocet_rokov)

print(f"{meno} {priezvisko} ma {vek} {slovo1} a o {pocet_rokov} {slovo2} rokov bude {vystup}")
