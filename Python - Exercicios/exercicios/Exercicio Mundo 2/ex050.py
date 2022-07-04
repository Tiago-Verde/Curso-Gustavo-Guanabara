# DESENVOLVA UM PROGRAMA QUE LEIA SEIS NUMEROS INTEIROS E MOSTRE A SOMA APENAS DAQUELES QUE FOREM PARES, SE O VALOR DIGITADOR FOR IMPAR, DESCONSIDERE
soma = 0
for c in range(0, 6):
    valor = int(input('Informe um valor: '))
    if valor % 2 == 0:
        soma = soma + valor
print(soma)
    