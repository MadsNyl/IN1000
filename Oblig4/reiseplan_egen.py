from time import sleep

# klasser
class Planlegg:
    def __init__(self):
        self.antall_reiser = 0
        self.reiseplan = {}
        self.reiser = []

    def start_planlegging(self):
        print('Planlegging startet.')
        self.antall_reiser = int(input('Hvor mange reiser vil du planlegge? '))
        for i in range(self.antall_reiser):
            reisemål = input('Velg et reisemål: ')
            self.reiser.append(reisemål)
            self.reiseplan[reisemål] = {}
            plagg = input('Velg et plagg du skal ha med: ')
            self.reiseplan[reisemål]['plagg'] = plagg
            reisedato = input('Velg en reisedato: ')
            self.reiseplan[reisemål]['reisedato'] = reisedato
            print(f'Reise planlagt for {reisemål}.')
        print(f'Dine reiser er planlagt for {self.reiser}.')
        sleep(1)

planlegg = Planlegg()

class SeReiseplan:
    def __init__(self):
        self.reiseplan = planlegg.reiseplan
    
    def se_reiseplan(self):
        reisemål = input('Velg et reisemål: ')
        detaljer = input('Hvis du vil se hvilket plagg du skal ha med, trykk "p"\nHvis du vil se reisedato, trykk "d"\nHvis du vil se hele reiseplanen, trykk "h": ')
        if detaljer == 'p':
            print(self.reiseplan[reisemål]['plagg'])
        elif detaljer == 'd':
            print(self.reiseplan[reisemål]['reisedato'])
        elif detaljer == 'h':
            print(self.reiseplan[reisemål])
        sleep(1)

# opprett instanser av klassene
reiseplan = SeReiseplan()

# velkomst
print('Hei, velkommen til din reiseplanlegger.')
sleep(1)
# velg hvilken klasse som skal iverksettes


while True:
    start_valg = input('For å planlegge en ny reise, trykk "p". \nFor å se en eksiterende plan, trykk "s": \nFor å avslutte programmet, skriv "avslutt": ')

    if start_valg == 'p':
        planlegg.start_planlegging()
    elif start_valg == 's':
        reiseplan.se_reiseplan()
    elif start_valg == 'avslutt':
        break
    else:
        print('Det er dessverre ikke et valg. Har du tastet inn riktig?')


