'''
# Listas Tuplas e Dicionários

lista = [1, 2, 3, 4, 5, ['Python','java']]
print(type(lista))
# Resultado --> <type 'list'>

print(lista)
# Resultado --> [1, 2, 3, 4, 5, ['Python', 'java']]

print(lista[1])
#Resultado

print(lista[:5])
#Resultado --> [1, 2, 3, 4, 5]

print('imprimindo os dados da segunda lista já existente --> ')
print(lista[5])
#Resultado -->  imprimindo os dados da segunda lista já existente -->  ['Python', 'java']

print('primeiro dado da segunda lista dentro de uma outra lista --> ' +  lista[5][0])
#Resultado --> segundo dado da segunda lista dentro de uma outra lista --> java

dicionarios = dict()
ouAssim = {'valor1': 1, 'valor2': 2}
#Resultado --> type(dicionarios)
#Resultado --> type(ouAssim)
#Resultado --> dict

print(dicionarios)
print(ouAssim)
# Resultado --> {}
# Resultado --> {'valor1': 1, 'valor2': 2}

print('pegando o primeiro valor do dicionário')
print(ouAssim['valor1'])
print('pegando o segundo valor do dicionário')
print(ouAssim['valor2'])
#Resultado --> pegando o primeiro valor do dicionário
#Resultado --> 1
#Resultado --> pegando o segundo valor do dicionário
#Resultado --> 2

dicionarios = {'lista':[1, 2, 3], 'str':'ola'}
print(dicionarios)
#Resultado --> {'lista': [1, 2, 3], 'str': 'ola'}

print(dicionarios['lista'])
#Resultado --> [1, 2, 3]

print(dicionarios['str'])
#Resultado -> ola

tupla = (1, 2, 3)

print(tupla)
#Resultado -->  (1, 2, 3)

print(type(tupla))
#Resultado --> tuple

print('lista são mutáveis')
lista[0] = 7
print(lista)
#Resultado -->lista são mutáveis
#Resultado --> [7, 2, 3, 4, 5, ['Python', 'java']]

print('tuplas são imutáveis')
print(tupla)
tupla[0] = 5
print('impossível mudar o valor de um dado depois de já populado, somente trocando na declaração do mesmo.')
#Resultado que saíria no terminal -->

tuplas são imutáveis
(1, 2, 3)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-116-cd2d9f63f920> in <module>()
      1 print('tuplas são imutáveis')
      2 print(tupla)
----> 3 tupla[0] = 5
      4 print('impossível mudar o valor de um dado depois de já populado, somente trocando na declaração do mesmo.')

TypeError: 'tuple' object does not support item assignment
'''