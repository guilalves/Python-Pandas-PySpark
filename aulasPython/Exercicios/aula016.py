from math import trunc

num = float(input('Digite um numero para obter sua porção inteira: '))
print('A porção inteira de {} é: {}'.format(num, trunc(num))) # Ou pode-se usar int(num)
