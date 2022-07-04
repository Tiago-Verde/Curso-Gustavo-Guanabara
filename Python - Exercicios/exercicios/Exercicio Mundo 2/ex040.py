# CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE A MEDIA MOSTRANDO A SEGUINTE MENSAGEM NO FINAL
# MÉDIA ABAIXO DE 5.0 REPROVADO
# MÉDIA ENTRE 5.0 E 6.9 RECUPERAÇÃO
# MEDIA ACIMA DE 7.0 APROVADO

nota1 = float(input('Qual a primeira nota do aluno: '))
nota2 = float(input('Qual a segunda nota do aluno: '))
nota3 = float(input('Qual a segunda nota do aluno: '))
nota4 = float(input('Qual a segunda nota do aluno: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print('Aluno Aprovado')
else:
    recuperacao = float(input('qual a nota da prova de recuperação '))
    mediaRecuperacao = (media + recuperacao) / 2

if mediaRecuperacao >=6:
    print('Aprovado em recuperação')
else:
    print('Reprovado')

#CÓDIGO EM PYTHON

    
