from math import sin, cos, tan, radians

an = float(input('Digite o ângulo: '))
seno = sin(radians(an))
print('O ângulo {} tem o seno de {:.2f}'.format(an, seno))

cos = cos(radians(an))
print('O ângulo {} tem o cosseno de {:.2f}'.format(an, cos))

tan = tan(radians(an))
print('O ângulo {} tem a tangente de {:.2f}'.format(an, tan))