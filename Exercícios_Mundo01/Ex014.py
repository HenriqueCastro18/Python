dias = int(input('Quantos dias foi usado o carro: '))
km = float(input('Quantos kms você rodou: '))

resulD = dias * 60
resulKm = km * 0.15 

total = resulD + resulKm

print('Considerando que você usou o carro por {} dias, e rodou {}KM. O valor total a ser pago é de R$ {:.2f}'.format(dias,km,total))
