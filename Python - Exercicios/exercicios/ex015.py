# ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO ALUGADO E A QUANTIDADE DE DIAS PELOS QUAIS ELE FOI ALUGADO
# CALCULE O PREÇO A PAGAR SABENDO QUE O CARRO CUSTA R$ 60,00 POR DIA E O KM RODADO É DE 0,15 CENTAVOS

kmPercorridos = float(input('Quantos km foram percorridos: '))
qtdDias = int(input('Por quantos dias o carro foi alugado: '))

valorPagar = (kmPercorridos * 0.15) + (qtdDias*60.0)

print('O valor a ser pago pelo carro é de R${}'.format(valorPagar))
