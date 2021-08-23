tall_liste = [1, 3, 5]
tall_liste.append(7)

print(tall_liste[0])
print(tall_liste[2])

navn_liste = []

for i in range(4):
    navn = input('Skriv inn et navn: ').lower()
    navn_liste.append(navn)

mitt_navn = 'mads'

if mitt_navn in navn_liste:
    print('Du husket meg!')
else:
    print('Har du glemt meg?')
