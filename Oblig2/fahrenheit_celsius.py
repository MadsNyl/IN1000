fahrenheit = input('Gi meg en temperatur i fahrenheit: ')

def fahrenheit_til_celsius(temperatur):
    print(temperatur)
    celsius = (int(temperatur) - 32) * 5/9
    formatert_celsius = "{:.2f}".format(celsius)
    print(formatert_celsius)

fahrenheit_til_celsius(fahrenheit)