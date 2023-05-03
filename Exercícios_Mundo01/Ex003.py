print('='*30)
print(9**(1/2)) # raiz quadrada
print('='*30)
print(9**(1/3)) # raiz cubica 
print('='*30)

name = input('Qual seu nome ?')

print('Seja bem vindo(a) {:<20}!'.format(name)) # alinhado  a esquerda e 20 espaços a frente contanto com a primeira letra
print('Seja bem vindo(a) {:<20}!'.format(name)) # alinhado a direita e 20 espaços a atras contanto com a primeira letra
print('Seja bem vindo(a) {:^20}!'.format(name)) #alinhado no meio e 20 espaços dividios em frente e a atras contanto com a primeira letra
print('Seja bem vindo(a) {:=^20}!'.format(name)) #alinhado no meio  e 20 = na frente e atras contanto com a primeira letra

n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
s = n1 + n2
m = n1 - n2
v = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('A soma é: {} a subtração é: {} a multiplicação é: {} a divisão é: {:.3f} a divisão inteira é: {} e o expoente é: {:.4f}'.format(s,m,v,d,di,e))