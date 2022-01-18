# FAÇA UM PROGRAMA QUE LEIA UM ANGULO QUALQUER E MOSTRE NA TELA O VALOR DO SENO COSENO E TANGENTE DESSE ANGULO
import math

ang = int(input('Informe um angulo: '))
angulo = math.radians(ang)
coseno = math.cos(angulo)
seno = math.sin(angulo)
tangente = math.tan(angulo)
print('O valor do coseno é {:.2f} do seno é {:.2f} e da tangente é  {:.2f}'.format(coseno, seno, tangente))



