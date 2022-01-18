# FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO E DO CATETO ADJACENTE DE UM TRINGULO RETANGULO E CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA
import math
catetoOposto = float(input('Informe o cateto oposto: '))
catetoadjacente = float(input('Informe o cateto adjacente: '))
hipotenusa = math.hypot(catetoOposto, catetoadjacente)
print('A hipotenusa é {}'.format(hipotenusa))
