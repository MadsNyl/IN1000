matplan = {
    'kari': {
        'frokost': 'brød',
        'lunsj': 'suppe',
        'middag': 'kylling'
    },
    'kåre': {
        'frokost': 'knekkebrød',
        'lunsj': 'egg',
        'middag': 'suppe'
    },
    'guri': {
        'frokost': 'polarbrød',
        'lunsj': 'suppe',
        'middag': 'kjøttkaker'
    } 
}

def hent_matplan(beboer, måltid):
    if beboer in matplan:
        try:
            if måltid == 'null':
                print(matplan[beboer])
            else:
                print(matplan[beboer][måltid])
        except:
            print('Måltid ikke registrert')
    else:
        print('Beboer ikke registrert')

while True:
    beboer, måltid = input('Navn og måltid ("null" for alle måltid): ').split(',')
    hent_matplan(beboer, måltid)


