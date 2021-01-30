from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento..: '))
idade = atual - nasc

if idade <= 9:
    print('Idade..: {} - Classificação MIRIN'.format(idade))
elif idade <= 14:
    print('Idade..: {} - Classificação INFANTIL'.format(idade))
elif idade <= 19:
    print('Idade..: {} - Classificação JUNIOR'.format(idade))
elif idade <= 25:
    print('Idade..: {} - Classificação SENIOR'.format(idade))
else:
    print('Idade..: {} - Classificação MASTER'.format(idade))
