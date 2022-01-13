# ESTRUTURAS CONDICIONAIS

tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
    print('Seu carro ainda é novo')
else: 
    print('Seu carro já está começando a ficar velho')


nome = str(input('Qual o seu nome?')).upper()
if nome == 'TIAGO':
    nomeFinal = nome.capitalize()
    print('Que nome lindo você tem. Bom dia {}'.format(nomeFinal))
else:
    nomeFinal = nome.capitalize()
    print('Tenha um bom dia {}'.format(nomeFinal))
print('Vamos detonar nesse dia!!!!')


nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print('Aluno aprovado!!!')
else:
    print('Aluno reprovado')
print('Média final de: {}'.format(media))