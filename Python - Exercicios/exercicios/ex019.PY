# UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO. FAÇA UM PROGRAMA QUE AJUDE ELE LENDO OS NOMES DELES E ESCREVENDO O NOME DO ESCOLHIDO
import random

aluno1 = input('Informe o nome do aluno: ')
aluno2 = input('Informe o nome do aluno: ')
aluno3 = input('Informe o nome do aluno: ')
aluno4 = input('Informe o nome do aluno: ')

listaNome = [aluno1, aluno2, aluno3, aluno4]
sorteio = random.choice(listaNome)
print('O aluno sorteado foi {}'.format(sorteio))
