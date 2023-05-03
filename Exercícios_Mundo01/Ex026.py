from random import randint
from time import sleep

num = int(input('Tente adivinhar o numero[0-5]: '))
numr = randint(0, 5)
print('Processando...')
sleep(.5)

if(num == numr):
    print('-=-'*25)
    print('Eu pensei no numero {} e você disse {}'.format(numr, num))
    print('Você acertou !!')
    print('-=-'*25)

elif(num >= 6):
    print('-=-'*25)
    print('Lembre-se o numero deve se de 0 a 5 \nTENTE NOVAMENTE')
    print('-=-'*25)

else:
    print('-=-'*25)
    print('Você errou !!')
    print('Eu pensei no numero {} e não no {}'.format(numr, num))
    print('-=-'*25)


