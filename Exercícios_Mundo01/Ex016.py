from math import hypot

co = float(input('Diga-me o valor do cateto oposto: '))
ca = float(input('Diga-me o valor do cateto adjacente: '))

hipo = hypot(co, ca)

print('O valor da Hipotenusa, considerando que o cateto oposto é de: {} e o cateto adjacente é de: {} a Hipotenusa é {:.2f}'.format(co, ca, hipo))