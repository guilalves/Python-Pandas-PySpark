n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1 + n2) / 2

if media >= 7:
    print('A média do aluno é de: {}, Passou !'.format(media))
else:
    print('A média do aluno é de: {}, Reprovou !'.format(media))