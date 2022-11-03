usuario = input('Qual seu nome?: ')
print('<----------------------->')
print('Bem vindo', usuario,'eu me chamo Henrique, e irei te auxiliar nesse aplicativo!')
print('<----------------------->')
comecar = input('Podemos começar? s/n?: ')
print('<----------------------->')

if comecar == 'n':
    print('<----------------------->')
    print('Okay, estarei pronto mais tarde!')
    print('<----------------------->')
    


elif comecar == 's':
    print('Aqui iremos criar uma chaves aleatoria, para deixar suas contas mais seguras!')
    print('<----------------------->')
    
    funcao = input('Digite chave para gerar a sua!: ')


    if funcao == 'chave':
        import random
        import math
        import string
        abc = string.ascii_letters
        punctuation = string.punctuation
        ascii_punctuation = abc + punctuation
        
    print('<----------------------->')
    print(''.join(random.SystemRandom().choices(ascii_punctuation, k=42)))
    print('<----------------------->')

    print('ESPERO QUE TENHA SIDO UTIL!')
