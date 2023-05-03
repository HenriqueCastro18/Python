salario = float(input('Insira seu salario: '))
porcento = 15 / 100
resul = salario * porcento + salario

print('O salario com um aumento de 15% é de R${:.2f}'.format(resul))