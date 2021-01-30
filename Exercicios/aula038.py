num = int(input('Digite um numero inteiro: '))
print('Escolha uma das bases para convesão:')

conversor = int(input('''
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
Sua opcao: '''))

if conversor == 1:
    print('{} convertido para BINÁRIO e igual a {}'.format(num, bin(num)[2:]))
elif conversor == 2:
    print('{} convertido para BINÁRIO e igual a {}'.format(num, oct(num)[2:]))
elif conversor == 3:
    print('{} convertido para BINÁRIO e igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção invalida!')
