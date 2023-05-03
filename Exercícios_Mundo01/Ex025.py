n = str(input('Digite seu nome completo: ')).strip()
name = n.split()

print('Seu primeiro nome é {}'.format(name[0]))
print('Seu ultimo nome é {}'.format(name[len(name)-1]))
