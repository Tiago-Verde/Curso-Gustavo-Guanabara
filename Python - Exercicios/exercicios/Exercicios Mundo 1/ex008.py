# ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS E O EXIBA CONVERTIDO EM CENTIMETROS E MILIMETROS

metros = float(input('Informe a medida em metros: '))
centimetros = metros*100
milimetros = metros*1000
print('A medida informada em centimetros é {:.2f} cm e a medida em milimetros é de {:.2f} mm'.format(centimetros, milimetros))
