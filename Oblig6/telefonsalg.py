def innlesing(filnavn):
    with open(filnavn, 'r') as f:
        ordbok = {}
        for linje in f:
            navn, tall = linje.split()
            ordbok[navn] = int(tall)
        return ordbok

ordbok = innlesing('Oblig6/salgstall.txt')

def maanedensSalgsPerson(ordbok):
    høyestSalg = [(verdi, nøkkel) for nøkkel, verdi in ordbok.items()]
    tall, navn = max(høyestSalg)
    return tall, navn

def totalAntallSalg(ordbok):
    sum = 0
    for nøkkel in ordbok:
        verdi = ordbok[nøkkel]
        sum += verdi
    return sum

def gjennomsnittSalg(ordbok):
    sum = totalAntallSalg(ordbok)
    gjennomsnitt = sum / len(ordbok)
    return gjennomsnitt

def hovedprogram(ordbok):
    tall, navn = maanedensSalgsPerson(ordbok)
    print(f'Maanedes selger er {navn} med {tall} salg.')
    print(f'Aktivere selgere denne maaneden: {len(ordbok)}')
    sum = totalAntallSalg(ordbok)
    print(f'Totalt antall salg: {sum}')
    gjennomsnitt = gjennomsnittSalg(ordbok)
    gjennomsnitt = "{:.2f}".format(gjennomsnitt)
    print(f'Gjennomsnittlig antall salg per salgsperson: {gjennomsnitt}')

hovedprogram(ordbok)

