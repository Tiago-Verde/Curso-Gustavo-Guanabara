# UM PROFESSOR QUER SORTEAR A ORDEM DE APRESENTAÇÃO DE SEUS TRABALHOS. FAÇA UM PROGRAMA QUE LEIA O NOME DOS 4 ALUNOS E MOSTRE A ORDEM SORTEADA
import random

aluno1 = input('Informe o nome do aluno: ')
aluno2 = input('Informe o nome do aluno: ')
aluno3 = input('Informe o nome do aluno: ')
aluno4 = input('Informe o nome do aluno: ')

listaNome = [aluno1, aluno2, aluno3, aluno4]

random.shuffle(listaNome)
print('O aluno sorteado foi {}'.format(listaNome))