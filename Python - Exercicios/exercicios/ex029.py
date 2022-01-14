# ESCREVA UM PROGRAMA QUE LEIA A VELOCIDADE DE UM CARRO, SE ELE ULTRAPASSAR 80KM MOSTRE UMA MENSAGEM DIZENDO QUE ELE SERÁ MULTADO
# A MULTA IRA CUSTAR R$ 7,00 POR CADA KM ACIMA DO LIMITE E ELA DEVE SER APRESENTADA NA TELA

velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
    multa = (velocidade-80) * 7
    print('Você acaba de ser multado, e o valor de sua multa é de R$ {},00'.format(multa))
print('Faça uma boa viagem. E dirija com segurança')