# REFAÇA O DESAFIO NUMERO 9 MOSTRANDO A TABUADA QUE O USUARIO ESCOLHER SO QUE AGORA UTILIZANDO UM LAÇO FOR
tabuada = int(input('Qual tabuada você quer saber? '))
for c in range(0, 11):
    resultado = tabuada * c
    print('{} x {} = {}'.format(tabuada, c, resultado))