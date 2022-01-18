# ESCREVA UM PROGRAMA PARA APROVAR O EMPRESTIMO BANCARIO PARA A COMPRA DE UMA CASA. O PROGRAMA VAI PERGUNTAR O VALOR DA CASA. 
# O SALARIO DO COMPRADOR E EM QUANTOS ANOS ELE VAI PAGAR. CALCULE O VALOR DA PRESTAÇÃO MENSAL SABENDO QUE ELA NÃO PODERÁ 
# EXCEDER 30% DO SALARIO OU ENTÃO O EMPRESTIMO SERÁ NEGADO

valorCasa = float(input('Qual o valor da casa que você está comprando: '))
salario = float(input('Qual o seu salario? '))
pagamento = int(input('Em quantos anos você pretende realizar o pagamento? '))

numeroParcelas = pagamento / 12
valorParcelas = valorCasa / numeroParcelas
