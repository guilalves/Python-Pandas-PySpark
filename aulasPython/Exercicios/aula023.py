from time import sleep

n = int(input('Informe um numero: '))
print('Analisando seu numero {}'.format(n))
sleep(1)
u = n // 1 % 10
d = n // 10 % 10
c = n //100 % 10
m = n // 1000 % 10 

print('{} Unidade'.format(u))
print('{:.0f} Dezena'.format(d))
print('{:.0f} Centena'.format(c))
print('{} Milhar'.format(m))