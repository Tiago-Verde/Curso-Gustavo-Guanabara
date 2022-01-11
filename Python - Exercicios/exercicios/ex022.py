# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA E MOSTRE
    # 1 - O NOME COM TODAS AS LETRAS MAIUSCULAS
    # 2 - O NOME COM TODAS AS LETRAS MINUSCULAS
    # 3 - QUANTAS LETRAS AO TODO SEM CONSIDERAR O ESPAÇO
    # 4 - QUANTAS LETRAS TEM O PRIMEIRO NOME

nome = input('Qual o seu nome completo ')
maiuscula = nome.upper()
print('O seu nome com letras maisuculas é {}'.format(maiuscula))

print('O seu nome com todas as letras minusculas é: ', nome.lower())

lista = nome.split()
junta = ''.join(lista)
qtsLetras = len(junta)

print('O seu nome tem um total de {} letras sem contar os espaços em branco'. format(qtsLetras))

lista = nome.split()
primeiro = lista[0]
qtsLetrasNome = len(primeiro)

print('O seu primeiro nome tem um total de {} letras'.format(qtsLetrasNome))
