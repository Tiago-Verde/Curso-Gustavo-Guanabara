#RESOLUÇÃO ALTERNATIVA PARA EXERCICIO -> CRIE UM PROGRAMA DE COMPUTADOR QUE JOGUE JOKENPO COM VOCÊ

from random import randint

jogadas = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[ 0 ] - Pedra
[ 1 ] - Papel
[ 2 ] - Tesoura ''')

usuario = int(input('Qual a sua jogada?? '))
print('O computador jogou {}'.format(jogadas[computador]))
print('-=' *11)
print('O jogador jogou {}'.format(jogadas[usuario]))
print('-=' *11)


if (computador == 0) and (usuario == 2):
    print('Como você já sabe {} quebra {} e nesse caso eu ganhei'.format(jogadas[computador], jogadas[usuario]))
elif (computador == 2) and (usuario == 1):
    print('Como você já sabe {} corta {} e nesse caso eu ganhei'.format(jogadas[computador], jogadas[usuario]))
elif (computador == 1) and (usuario == 0):
    print('Como você já sabe {} enbrula {} e nesse caso eu ganhei'.format(jogadas[computador], jogadas[usuario]))

elif (computador == 2) and (usuario == 0):
    print('Como você já sabe {} é quebrada por {} e nesse caso você ganhou'.format(jogadas[computador], jogadas[usuario]))
elif (computador == 1) and (usuario == 2):
    print('Como você já sabe {} é cortado pela {} e nesse você ganhou'.format(jogadas[computador], jogadas[usuario]))
elif (computador == 0) and (usuario == 1):
    print('Como você já sabe {} é embrulhada pelo {} e nesse caso você ganhou'.format(jogadas[computador], jogadas[usuario]))
else:
    print('Deu empate, vamos jogar novamente?? ')

