# FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO E MOSTRE
# 1 - QUANTAS VEZES APARECE A LETRA "A"
# 2 - EM QUE POSIÇÃO ELA APARECE PELA PRIMEIRA VEZ
# 3 - EM QUE POSIÇÃO ELA APRECE PELA ULTIMA VEZ

frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes nessa frase'.format(frase.count('A')))
print('A letra A aparece pela primeira vez na posição {}'.format(frase.find('A')+1))
print('A letra A aparece pela ultima vez na frase na posição {}'.format(frase.rfind('A')+1))

