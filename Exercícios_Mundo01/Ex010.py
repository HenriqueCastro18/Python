larg = float(input('Insira a largura de uma parede EM METROS: '))
alt = float(input('Agora insira a altura desta parede EM METROS: '))

area = larg * alt
tinta =  area / 2

print('A largunra da parede é de {} a altura é de {}, a área total é {}m² precisa de {}L de tinta para pintar a parede toda'.format(larg,alt,area,tinta))