varer = {
    'melk': 14.90,
    'brød': 24.90,
    'yoghurt': 12.90,
    'pizza': 39.90
}

print(varer)

ny_vare1 = input('Legg til vare: ')
ny_pris1 = input('Legg til pris: ')

ny_vare2 = input('Legg til vare: ')
ny_pris2 = input('Legg til pris: ')

varer[ny_vare1] = float(ny_pris1)
varer[ny_vare2] = float(ny_pris2)

print(varer)