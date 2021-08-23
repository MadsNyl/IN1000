print('Hei student!')

navn = input('Hva er navnet ditt? ')

print('Hei ' + navn)

tall1, tall2 = input('Gi meg to heltall er du snill: ').split(',')
tall1, tall2 = [int(tall1), int(tall2)]

differanse = tall1 - tall2

print('Differansen er: ', differanse)

nytt_navn = input('Vennligst gi meg et nytt navn: ')

sammen = navn + '' + nytt_navn

print(sammen)

sammen = navn + ' og ' + nytt_navn

print(sammen)
