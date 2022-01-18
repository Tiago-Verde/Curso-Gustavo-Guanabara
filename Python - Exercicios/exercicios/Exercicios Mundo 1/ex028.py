# ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR PENSAR EM UM NUMERO DE 0 A 5 E PEÇA PARA O USUARIO TENTAR DESCOBRIR QUEL O NUMERO
# O PROGRAMA DEVERA ESCREVER SE O USUARIO ACERTOU OU ERROU O NUMERO SORTEADO
import random

sorteio = random.randint(0, 5)

palpite = int(input('Adivinha qual numero estou pensando entre 0 e 5: '))
if palpite == sorteio:
    print('Parabens, você acertou o numero! Mizeravi')
else:
    print('Não foi dessa vez!!!')
print(sorteio)