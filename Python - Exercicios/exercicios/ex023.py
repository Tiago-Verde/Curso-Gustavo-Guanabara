# FAÇA UM PROGRAMA QUE LEIA UM NUMERO DE 0 A 9999 E MOSTRE NA TELA CADA UM DOS DIGITOS SEPARADOS
# EX: DIGITO 1834
# UNIDADE 4
# DEZENA 3
# CENTENA 8
# MILHAR 1

numero = int(input('Informe um numero qualquer entre 0 e 9999: '))
un = numero // 1 % 10
dez = numero // 10 % 10
cent = numero // 100 % 10
Milh = numero // 1000 % 10
print('O numero informado tem {} unidades'.format(un))
print('O numero informado tem {} dezenas'.format(dez))
print('O numero informado tem {} centenas'.format(cent))
print('O numero informado tem {} milhar'.format(Milh))


