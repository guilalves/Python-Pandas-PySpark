algo = input('Digite algo: ')

print('O tipo primtivo desse valor é {}'.format(type(algo)))
print('Só te espaços ? {} '.format(algo.isspace()))
print('É um número ? ', algo.isnumeric())
print('É um alfabético ? {}'.format(algo.isalpha()))
print('É um alfanumérico ? {}'.format(algo.isalnum()))
print('Está em maiúsculas ? {}'.format(algo.isupper()))
print('Está em minúsculas ? {}'.format(algo.islower()))
print('Está capitalizada ? {}'.format(algo.istitle()))