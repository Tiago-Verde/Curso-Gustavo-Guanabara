# FAÇA UM PROGRAMA QUE LEIA A ALTURA E A LARGURA DE UMA PAREDE EM METROS CALCULE SUA AREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTA-LA
# SABENDO QUE CADA LITRO DE TINTA PINTA UMA AREA DE 2M²

base = float(input('Informe qual a largura da parede: '))
altura = float(input('Informe a altura da parede: '))
area = base*altura
print('Você tem uma area de {}'.format(area))
rendimento = area/2
print('Será necessário {} litros de tinta para pintar sua parede'.format(rendimento))