import random

print(random.random()) # Valor 0.0 até 1.0
print(random.uniform(4,10)) # Valor decimal do mínimo ao máximo 
print(random.randint(12,55)) # Valor inteiro do mínimo ao máximo
cores = ['verde','vermelho','azul']
print(random.choice(cores)) # Escolher uma opção dentro de uma fonte cartas_
cartas_de_um_baralho = ['carta1','carta2','carta3','carta4','carta5',]# Para embaralhar a sequencia passada! 
random.shuffle(cartas_de_um_baralho) 
print(cartas_de_um_baralho)
