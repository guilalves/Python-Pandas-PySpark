from math import hypot

co = float(input('Digite o numero do cateto oposto: '))
ca = float(input('Digite o numero do cateto oposto: '))
hi = hypot(co, ca)
print('A hipotenusa das somas dos quadrados dos catetos é : {:.2f}'.format(hi))