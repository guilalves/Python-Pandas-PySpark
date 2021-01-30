from math import sin, cos, tan, radians

angulo = float(input('Digite um ângulo para se obter o seu seno, cosseno e tangente: '))
seno = sin(radians(angulo))
coss = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O seno do angulo {} é {:.2f}'.format(angulo, seno))
print('O cosseno do angulo {} é {:.2f}'.format(angulo, coss))
print('A tangente do angulo {} é {:.2f}'.format(angulo, tangente))