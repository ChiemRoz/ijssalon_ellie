prijzen = {
    "aardbei" : 3,
    "vanille" : 4,
    "chocolade" : 5
}

aanbieding = prijzen["aardbei"] * 0.8
print(prijzen["aardbei"])

reclame_tekst = f"Vandaag in de aanbieding: aardbei-ijs, 1 liter – slechts € {aanbieding}"
print(reclame_tekst)

print(f"Vandaag in de aanbieding: aardbei-ijs, 1 liter - slechts € {aanbieding}")
print(reclame_tekst)

reclame_tekst2 = reclame_tekst[:62]
print(reclame_tekst2)

reclame_tekst3 = reclame_tekst2.upper()
print(reclame_tekst3)

reclame_tekst4 = reclame_tekst3.split(" ")
print(reclame_tekst4)

for el in reclame_tekst4:
    if len(el) > 4: 
        print(el.upper())
    else:
        print(el.lower())
        