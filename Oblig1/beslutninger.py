svar = input('Hei, har du lyst på en brus? ').lower()


while True:

    if svar == 'ja':
        print('Her har du en brus!')
        break
    elif svar == 'nei':
        print('Den er grei.')
        break
    else:
        svar = input('Det forstod jeg ikke helt. Kan du gjenta det? ').lower()