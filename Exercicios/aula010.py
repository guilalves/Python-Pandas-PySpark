real = float(input('Quando dinheiro você tem para converter em dólares? R$ '))
dolar_US = real / 5.05
dolar_CN = real / 3.49
euro = real / 6.12
print('Com R$ {:.2f} Reais você pode comprar US$ {:.2f} Dólares'.format(real, dolar_US))
print('Com R$ {:.2f} Reais você pode comprar CAD$ {:.2f} Dólares canadense'.format(real, dolar_CN))
print('Com R$ {:.2f} Reais você pode comprar {:.2f} Euros'.format(real, euro))