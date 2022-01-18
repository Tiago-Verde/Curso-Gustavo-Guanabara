# FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO MOSTRANDO EM SEGUIDA O PRIMEIRO E O ULTIMO NOME SEPARADAMENTE
nome = str(input('Informe seu nome completo: ')).strip().upper()
lista = nome.split()
print('Seu primeiro nome é {}'.format(lista[0]))
print('Seu ultimo nome é {}'.format(lista[len(lista)-1]))

