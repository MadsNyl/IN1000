antall_reiseplaner = 2

steder = []
klesplagg = []
avreisedatoer = []
reiseplan = []

for i in range(antall_reiseplaner):
    print(f'La oss planlegge {antall_reiseplaner} reiser, en om gangen.')
    sted = input('Skriv et reisemål: ')
    steder.append(sted)
    plagg = input('Skriv inn ett plagg: ')
    klesplagg.append(plagg)
    avreisedato = input('Skriv inn en avreisedato: ')
    avreisedatoer.append(avreisedato)
    antall_reiseplaner -= 1

reiseplan.append(steder)
reiseplan.append(klesplagg)
reiseplan.append(avreisedatoer)

for liste in reiseplan:
    print(liste)

i1, i2 = input('Velg reiseplan: ').split(',')
i1, i2 = [int(i1), int(i2)]

print(reiseplan[i1])
print(reiseplan[i1][i2])



