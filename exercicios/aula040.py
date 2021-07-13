from datetime import date

ano = int(input('Ano de nascimento: '))
# atual = int(date.today().year) # funciona assim
data = date.today()
atual = int('{}'.format(data.year))  # ou assim
idade = (atual - ano)
print('Sua idade: {}'.format(idade))

if idade < 18:
    qty_anos = (18 - idade)
    print('Falta {} anos para voce se alistar!'.format(qty_anos))
elif idade > 18:
    qty_anos = (idade - 18)
    print('Ja passou {} anos de voce se alistar!'.format(qty_anos))
elif idade == 18:
    print('Ja esta na hora de se alistar!')
