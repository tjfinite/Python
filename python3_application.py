def vstupne_parametre():
    dochodkovy_vek = 86
    meno = input('Meno:')
    priezvisko = input("Priezvisko:")
    while True: #Kontrola datoveho typu parametru vek
        vek = input("Vek:")
        try:
            vek = int(vek)
            break
        except ValueError:
            print("Vek musi byt cele cislo!")
    return meno, priezvisko, vek, dochodkovy_vek

def vystupne_parametre(meno, priezvisko, vek, dochodkovy_vek):
    pocet_rokov_do_dochodku = dochodkovy_vek - vek
    if vek < 18: #Kontrola veku do 18 rokov
        print(f"{meno} este nie je v produktivnom veku.")
    elif vek >= 86: #Kontrola dosiahnuteho dochodkoveho veku 
        print(f"{meno} uz ma dochodkovy vek.")  
    else:
        stylizovane_slovo = stylizacia_slova_rok(pocet_rokov_do_dochodku)
        print(f"{meno} {priezvisko} ma {vek} rokov a o {pocet_rokov_do_dochodku} {stylizovane_slovo} bude mat {dochodkovy_vek}, co je dochodkovy vek.")
    return pocet_rokov_do_dochodku

def stylizacia_slova_rok(pocet_rokov_do_dochodku):
    if pocet_rokov_do_dochodku == 1:
        stylizovane_slovo = "rok"
    elif pocet_rokov_do_dochodku > 1 and pocet_rokov_do_dochodku < 5:
        stylizovane_slovo = "roky"
    else:
        stylizovane_slovo = "rokov"
    return stylizovane_slovo

meno, priezvisko, vek, dochodkovy_vek = vstupne_parametre()
vystupne_parametre(meno, priezvisko, vek, dochodkovy_vek)
