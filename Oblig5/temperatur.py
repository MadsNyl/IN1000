temperaturer = []

with open('Oblig5/temperatur.txt', 'r') as f:
    for linje in f:
        temperaturer.append(int(linje))


def gjsnittAvTemp(liste):
    sum = 0
    for obj in liste:
        sum += (obj)
    gjsnitt = sum / len(liste)
    return gjsnitt

print(gjsnittAvTemp(temperaturer))

