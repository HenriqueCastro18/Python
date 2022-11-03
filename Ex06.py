contas = ['']
usuario = input('Qual seu nome?: ')
print('Bem vindo', usuario, 'Eu me chamo Henrique. irei te auxiliar nesse programa!')

comecar = input('Podemos começar? s/n: ')

if comecar == 'n':
    print('Okay. Estarei pronto quando quiser!')


elif comecar == 's':
    print('<------------------------------------------------------------>')
    print('Irei te ajudar em contas de matemática com valores inteiros')
    print('<------------------------------------------------------------>')
    print('Para acessar as contas, escreva extamente assim: "mais, menos, vezes, dividir, fatorial, maior/menor, regra_de_tres, sen/cos/tang"')
    print('<------------------------------------------------------------>')
    contas = input('Vamos lá. Qual conta quer que eu resolva?: ')


    if contas == 'mais':
        primeiro_valor = int(input('Digite o primeiro valor: '))
        segundo_valor = int(input('Digite o segundo valor: '))
        resultado_soma = primeiro_valor + segundo_valor
        print('O resultado é:', resultado_soma)

    if contas == 'menos':
        primeiro_valor = int(input('Digite o primeiro valor: '))
        segundo_valor = int(input('Digite o segundo valor: '))
        resultado_menos = primeiro_valor - segundo_valor
        print('O resultado é:', resultado_menos)

    if contas == 'vezes':
        primeiro_valor = int(input('Digite o primeiro valor: '))
        segundo_valor = int(input('Digite o segundo valor: '))
        resultado_vezes = primeiro_valor * segundo_valor
        print('O resultado é:', resultado_vezes)

    if contas == 'dividir':
        primeiro_valor = int(input('Digite o primeiro valor: '))
        segundo_valor = int(input('Digite o segundo valor: '))
        resultado_divisao = primeiro_valor / segundo_valor
        print('O resultado é:', resultado_divisao)

    if contas == 'fatorial':
        numero = int(input('Digite um número: '))
        if numero > 0:
            fatorial = 1
        for item in range(1, numero +1):
            fatorial = fatorial * item
        print('O resultado é:', fatorial)

    if contas == 'maior/menor':
        primeiro_valor = int(input('Digite o primeiro número: '))
        segundo_valor = int(input('Digite o segundo número: '))
        if int(primeiro_valor) > (segundo_valor):
            print('O primeiro valor é maior!')
        elif int(primeiro_valor) < (segundo_valor):
            print('O segundo valor é maior!')
        elif int(primeiro_valor) == (segundo_valor):
            print('Os valores são iguais!')

    if contas == 'regra_de_tres':
        primeiro_valor = int(input('Digite o primeiro valor: '))
        segundo_valor = int(input('Digite o segundo valor: '))
        terceiro_valor = int(input('Digite o terceiro valor: '))
        x = primeiro_valor * segundo_valor / terceiro_valor
        print('O resultado é: ',x)

    if contas == 'sen/cos/tang':
        import math
        angulo = float(input('Digite o ângulo desejado: '))
        seno = math.sin(math.radians(angulo))
        print('O ângulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
        cosseno = math.cos(math.radians(angulo))
        print('O ângulo de {} tem o COSSENO de {:.2f}'.format(angulo,cosseno))
        tangente = math.tan(math.radians(angulo))
        print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(angulo, tangente))

    else:
        print('Opção invalida')
        
    print('<------------------------------------------------------------>')
    print('OBRIGADO POR USAR O PROGRAMA! <3')
