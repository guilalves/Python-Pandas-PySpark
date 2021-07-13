from time import sleep
from random import randint
pc = randint(0,5)

def design():
    print('-=-' *20)


design()
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
design()

player = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(1)
if player != pc:
    print('Ganhei! Eu pensei no numero {} e não {}!'.format(pc, player))
else:
    print('VC Ganhou! eu pensei no mesmo no numero {} também!!!'.format(player))