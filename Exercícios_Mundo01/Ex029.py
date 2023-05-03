km = int(input('Digite o km da sua viagem: '))

if(km <= 200):
    valor = km * 0.5
    print('O valor total a ser pago é de R$: {:.2f}'.format(valor))

else:
    valor = km * 0.45
    print('O valor total a ser pago é de R$: {:.2f}'.format(valor))