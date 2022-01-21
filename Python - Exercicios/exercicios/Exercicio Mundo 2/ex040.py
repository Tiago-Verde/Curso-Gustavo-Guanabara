# CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE A MEDIA MOSTRANDO A SEGUINTE MENSAGEM NO FINAL
# MÉDIA ABAIXO DE 5.0 REPROVADO
# MÉDIA ENTRE 5.0 E 6.9 RECUPERAÇÃO
# MEDIA ACIMA DE 7.0 APROVADO

nota1 = float(input('Qual a primeira nota do aluno: '))
nota2 = float(input('Qual a segunda nota do aluno: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('Aluno reprovado, nota final {}'.format(media))
elif (media >= 5) and (media <= 6.9):
    print('Aluno de recuperação com média de {}'.format(media))
else:
    print('Aluno aprovado com média de {}'.format(media))
    
