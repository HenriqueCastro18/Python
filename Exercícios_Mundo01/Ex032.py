sal = float(input('Digite seu salario: '))

if(sal >= 1250):
    valor = sal * 10 / 100
    vf = valor + sal

else:
    valor = sal * 15 / 100
    vf = valor + sal

print('Seu aumento será de R$: {}, seu salario atualizado é de R$: {}'.format(valor, vf))