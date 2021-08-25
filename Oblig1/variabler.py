# slår sammen varibaler til strenger


print('Hei student!')

navn = input('Hva er navnet ditt? ')

# slår sammen variabel "navn" med en streng med en f-string
print(f'Hei {navn}')

# omgjør inputen fra streng til heltall
tall1, tall2 = input('Gi meg to heltall er du snill: ').split(',')
tall1, tall2 = [int(tall1), int(tall2)]

# regner differansen mellom tallene fra inputen
differanse = tall1 - tall2

# printer hva differenasen er
print(f'Differansen er: {differanse}')

# tar i mot input og slår sammen til en streng med mellomrom, og en med "og"
nytt_navn = input('Vennligst gi meg et nytt navn: ')

sammen = f'{navn} {nytt_navn}'

print(sammen)

sammen = f'{navn} og {nytt_navn}'

print(sammen)
