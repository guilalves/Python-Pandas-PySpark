dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km alugados? '))
aluguel = (dias * 60) + (km * 0.15)

print('O total a pagar é de R$ {:.2f}'.format(aluguel))