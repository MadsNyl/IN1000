#Nei, kan ikke slå sammen int og str i print. Må formattere b til str etter if sjekk. Eller bruke f-streng.

a = input("Tast inn et heltall! ")
b = int(a)
if b < 10:
    print(b + "Hei!")
