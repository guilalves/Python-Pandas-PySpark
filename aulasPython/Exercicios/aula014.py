# Conversor de temperaturas.

celsius = float(input('Informe a temperatura em °C: '))
convertC = (celsius * 1.8) + 32
print('A temperatura {} em Graus Celsius, é equivalente a {} em Graus fahrenheit'.format(celsius, convertC))
fahrenheit = float(input('Informe a temperatura em °F: '))
convertF = (fahrenheit - 32) / 1.8
print('A temperatura {} em Graus Fahrenheit, é equivalente a {} em Graus Celsius'.format(fahrenheit, convertF))