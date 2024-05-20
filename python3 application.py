meno = input('Meno:')
priezvisko = input("Priezvisko:")

while True:
    vek = input("Vek:")
    try:
        vek = int(vek)
        break
    except ValueError:
        print("Vek musi byt cele cislo!")

print(meno, priezvisko, "ma", vek, "rokov.")