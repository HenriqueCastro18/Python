#Simulador de dado
from ast import Try
from logging import exception
import random

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado?: '
    
    def Iniciar(self):
        resposta = input(self.mensagem)
        
        if resposta == 'sim' or resposta == 's':
            self.GerarValorDoDado()
        elif resposta == 'não' or resposta == 'n':
            print('Agradecemos a sua participação. Volte aqui quando quiser!')
        else:
            print('Favor digitar sim ou não!')


    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo,self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()
