speed = int(input('Digite a velocidade em numero inteiro: '))

if(speed <= 80):
    print('Você não foi multado. Pode seguir seu trajeto')

else:
    km = speed - 80
    total = km * 7
    print('Você passou {} acima do limite, o valor a multa a ser pago é de R$: {:.2f}'.format(km, total))