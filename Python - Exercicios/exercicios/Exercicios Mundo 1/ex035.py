# DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRES RETAS E DIGA SE ELAS PODEM FORMAR UM TRINGULO

lado1 = float(input('Informe o valor do primeiro lado:'))
lado2 = float(input('Informe o valor do segundo lado:'))
lado3 = float(input('Informe o valor do terceiro lado:'))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado2 + lado1:
    print('Pode ser formado um tringulo')
else:
    print('Não é possivel formar um tringulo')
