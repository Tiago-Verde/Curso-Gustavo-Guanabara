# DESENVOLVA UM PROGRAMA QUE LEIA AS DUAS NOTAS DE UM ALUNO E CALCULE A MEDIA E MOSTRE NA TELA

aluno = str(input('Qual o nome do aluno: '))
n1 = float(input('Informe a primeira nota do aluno: '))
n2 = float(input('Informe a segunda nota do aluno: '))
media = (n1+n2)/2
print('O aluno {} teve média {:.2}'.format(aluno, media))