preco = float(input('Insira o preço do protudo: '))


resul  = preco - (preco * 5 / 100)

print('Considerando o desconto de 5%. O valor final será de R${:.2f}'.format(resul))