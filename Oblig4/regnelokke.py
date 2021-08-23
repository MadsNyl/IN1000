tall_liste = []
minSum = []

while True:
    tall = input('Skriv et tall: ')
    tall_liste.append(int(tall))
    if int(tall) == 0:
        break

for tall in tall_liste:
    minSum.append(int(tall))

for tall in tall_liste:
    if min(tall_liste) == tall:
        print(f'Laveste tall: {tall}')

for tall in tall_liste:
    if max(tall_liste) == tall:
        print(f'Høyeste tall: {tall}')

minSum = sum(minSum)
print(minSum)