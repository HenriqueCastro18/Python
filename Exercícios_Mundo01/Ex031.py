n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))

menor = n1
maior = n1

#Menor

if(n2 < n1 and n2 < n3):
    menor = n2

elif(n3 < n1 and n3 < n2):
    menor = n3

#Maior

if(n2 > n1 and n2 > n3):
    maior = n2

elif(n3 > n1 and n3 > n2):
    maior = n3

print('O menor é {}'.format(menor))
print('O maior é {}'.format(maior))