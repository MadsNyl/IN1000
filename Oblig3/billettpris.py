def finn_billettpris():
    alder = int(input('Skriv inn alder: '))
    if alder <= 17:
        pris = 30
    elif 18 <= alder <= 62:
        pris = 50
    else:
        pris = 35
    
    print(f'Din billettpris: {pris}')

finn_billettpris()
finn_billettpris()
finn_billettpris()
finn_billettpris()