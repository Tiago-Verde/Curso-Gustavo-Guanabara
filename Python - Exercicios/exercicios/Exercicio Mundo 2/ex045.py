# CRIE UM PROGRAMA DE COMPUTADOR QUE JOGUE JOKENPO COM VOCÊ
import random

print('------------ Vamos jogar jogenpô -----------')
jogadas = ['Pedra', 'Papel', 'Tesoura']
computador = random.choice(jogadas)
print('Já pensei na minha jogado, preparado? ')

usuario = str(input('Qual a sua jogada?? '))

print('A minha jogada foi {} e a sua jogada foi {}'.format(computador, usuario))

if (computador == 'Pedra') and (usuario == 'Tesoura'):
    print('Como você já sabe {} quebra {} e nesse caso eu ganhei'.format(computador, usuario))
elif (computador == 'Tesoura') and (usuario == 'Papel'):
    print('Como você já sabe {} corta {} e nesse caso eu ganhei'.format(computador, usuario))
elif (computador == 'Papel') and (usuario == 'Pedra'):
    print('Como você já sabe {} enbrula {} e nesse caso eu ganhei'.format(computador, usuario))

elif (computador == 'Tesoura') and (usuario == 'Pedra'):
    print('Como você já sabe {} é quebrada {} e nesse caso você ganhou'.format(computador, usuario))
elif (computador == 'Papel') and (usuario == 'Tesoura'):
    print('Como você já sabe {} é cortado pela {} e nesse você ganhou'.format(computador, usuario))
elif (computador == 'Pedra') and (usuario == 'Papel'):
    print('Como você já sabe {} é embrulhada pelo {} e nesse caso você ganhou'.format(computador, usuario))
else:
    print('Deu empate, vamos jogar novamente?? ')




