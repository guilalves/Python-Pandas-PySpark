from time import sleep

nome = str(input('Digite seu nome completo: ')).strip()

print('Analisando seu nome...')
sleep(1)
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
separar = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separar[0], len(separar[0])))
