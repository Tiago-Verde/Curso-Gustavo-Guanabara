# FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NUMEROS IMPARES QUE SÃO MULTIPLOS DE 3 E QUE SE ENCONTRAM NO INTERVALO ENTRE 1 E 500

print('Vamos calcular numeros a soma de numeros impares no intervalo de 1 a 500')

soma = 0

for c in range (1,501, 2):
    if c % 3 == 0:
       soma = soma + c
print('A soma de todos os valores é {}'.format(soma))