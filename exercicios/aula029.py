velocity = float(input('What is the current speed of the car? '))
multa = 7.00

if velocity > 80:
    print('you were fined! You have exceeded the speed limit 80Km/h')
    multa = (velocity - 80) * 7
    print('You will have to pay R$ {:.2f}'.format(multa))
else:
    print('Good trip!')