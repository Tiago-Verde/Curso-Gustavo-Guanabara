# DESENVOLVA UM PROGRAMA QUE LEIA AS DUAS NOTAS DE UM ALUNO E CALCULE A MEDIA E MOSTRE NA TELA

aluno = str(input('Qual o nome do aluno: '))
n1 = int(input('Informe a primeira nota do aluno: '))
n2 = int(input('Informe a segunda nota do aluno: '))
media = (n1+n2)/2
print('O aluno {} teve média {}'.format(aluno, media))