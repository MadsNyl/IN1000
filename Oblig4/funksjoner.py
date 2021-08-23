def adder(tall1, tall2):
    sum = int(tall1) + int(tall2)
    return print(f'Sum av tall1 og tall2: {sum}')

adder(20, 40)
adder(20, 50)

def tellForekomst(minTekst, minBokstav):
    antall = 0
    for bokstav in minTekst:
        if bokstav == minBokstav:
            antall += 1
    return print(antall)


while True:

    tekst = input('Skriv inn tekst: ')
    bokstav = input('Velg en bokstav: ')
    tellForekomst(tekst, bokstav)


