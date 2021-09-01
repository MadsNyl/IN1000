# hent inn fahrenheit temperatur fra bruker
fahrenheit = input('Gi meg en temperatur i fahrenheit: ')

# omgjør fahrenheit til celcius
def fahrenheit_til_celsius(temperatur):
    print(temperatur)
    celsius = (int(temperatur) - 32) * (5/9)
    # formater til desimal med to tall
    formatert_celsius = "{:.2f}".format(celsius)
    print(formatert_celsius)

fahrenheit_til_celsius(fahrenheit)