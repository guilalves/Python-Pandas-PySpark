from datetime import date
now = date
ano = int(input('Qual ano vc quer analisar ? coloque 0 para usar o ano atual: '))
if ano == 0:
    ano = now.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} não é Bissesto'.format(ano))