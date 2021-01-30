distancia = float(input('Qual é a distancia da viagem ? '))
print('Você irá começar uma viagem de {}Km.'.format(distancia))
preco = 0
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('E o preco da sua passagem será de R${:.2f}'.format(preco))
"""preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45""" # exemplo de um if simplificado.