piso_salarial = 1250
sal = float(input('Qual é o salário do funcionário? R$'))
if sal >= piso_salarial:
    aumento = sal + (sal * 10/100)
else:
    aumento = sal + (sal * 15/100)
print('Seu novo salario é de {:.2f}'.format(aumento))