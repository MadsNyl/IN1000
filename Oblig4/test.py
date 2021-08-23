test = {}

test['test'] = {}

#print(test)

test['test']['ny'] = 'hei'
test['test']['endny'] = 'hei igjen'

#print(test)

reiseplan = {
    'oslo': {
        'plagg': ['genser', 'skjorte', 'tskjorte'],
        'reisedato': '5.mai'
    },
    'stockholm': {
        'plagg': 'skjorte',
        'reisedato': '5.april'
    },
    'paris': {
        'plagg': 'shorts',
        'reisedato': '5.januar'
    }
}

print(reiseplan['oslo']['plagg'][2])
