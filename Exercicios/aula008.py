distancia = float(input('Uma distância em metros: '))
km = distancia / 1000
hectômetro = distancia / 100
decametro = distancia / 10
decimetro = distancia * 10
centimetro = distancia * 100
milimetro = distancia * 1000
print('A medida de {} corresponde a '.format(distancia))
print('{} Km'.format(km))
print('{} hectômetro'.format(hectômetro))
print('{} decametro'.format(decametro))
print('{:.0f} decimetro'.format(decimetro))
print('{:.0f} centimetro'.format(centimetro))
print('{:.0f} milimetro'.format(milimetro))