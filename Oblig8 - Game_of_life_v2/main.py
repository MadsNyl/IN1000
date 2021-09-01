from spillebrett import Spillebrett


def main():
    rad, kolonne = input('Skriv inn dimmensjonene til brettet: ').split(',')
    rad, kolonne = [int(rad), int(kolonne)]
    spillebrett = Spillebrett(rad, kolonne)
    spillebrett.tegnBrett()

    kjør_program = True
    while kjør_program:
        bruker_input = input('For å kjøre en ny generasjon, press "enter".\nFor å avslutte, trykk "q": ')
        if bruker_input == '':
            spillebrett.oppdatering()
            spillebrett.tegnBrett()
        if bruker_input == 'q':
            kjør_program = False


if __name__ == "__main__":
    main()

    








