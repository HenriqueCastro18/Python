name = input('Me diga seu nome: ')
print('Ola {}  Seja bem vindo(a)'.format(name))

n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
valor = float(n1 + n2)

print(type(n1))

print('O resultado é {2}  da soma {0} + {1}'.format(n1,n2,valor))

n = input('Digite algo: ')
print(n.isnumeric(), 'Para numeros')
print(n.isalpha(), 'Para string')
print(n.isalnum(), 'Para numeros ou string e numeros e string')
print(n.isupper(), 'Para somente letras maiusculas')
print(n.islower(), 'Para somente tudos minusculo')
