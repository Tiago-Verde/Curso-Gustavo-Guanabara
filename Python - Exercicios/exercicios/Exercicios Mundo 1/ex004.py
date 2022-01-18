# FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE SEU TIPO PRIMITIVO E TODAS AS POSSIVEIS INFORMAÇÕES SOBRE ELA

print('Informação: ')
info1 = input('Digite algo no teclado: ')
print('Você digitou {}'.format(info1))
print('A informação digitada é do tipo {}'.format(type(info1)))
print('A informação digitada é numérica? {}'.format(info1.isnumeric()))
print('A informação digitada é alfabética? {}'.format(info1.isalpha()))
print('A informação digitada é decimal? {}'.format(info1.isdecimal()))
print('A informação digitada é ASCII? {}'.format(info1.isascii()))
print('A informação digitada é um digito? {}'.format(info1.isdigit()))
print('A informação digitada é "Printavel"? {}'.format(info1.isprintable()))



