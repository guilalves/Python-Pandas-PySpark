largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura * altura
tinta = area / 2
print('Sua parede tem a dimensão de {} X {} e sua área é de {:.1f}m2.'.format(largura, altura, area))
print('Para printar essa parede, vocẽ precisará de {:.1f}l de tinta.'.format(tinta))
