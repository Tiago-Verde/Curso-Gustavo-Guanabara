# ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO CONSIDERANDO O SEU PREÇO NORMAL E CONDIÇÃO DE PAGAMENTO
# A VISTA DINHEIRO OU CHEQUE 10% DE DESCONTO
# A VISTA NO CARTÃO 5% DE DESCONTO
# EM DUAS VEZES NO CARTÃO PREÇO NORMAL
# 3X OU MAIS NO CARTÃO 20% DE JUROS

valorProduto = float(input('Qual o valor do produto? '))
modoDePagamento = int(input('Qual será a forma de pagamento? Tecle 1 para dinheiro ou cheque, 2 para cartão a vista, 3 para parcelar em duas vezes no cartão ou 4 para parcelar em mais de 3 vezes '))


if (modoDePagamento == 1):
    novoValor = valorProduto - (valorProduto * 10 / 100)
    print('O valor a ser pago é de R$ {}'.format(novoValor))
elif (modoDePagamento == 2):
    novoValor = valorProduto - (valorProduto * 5 / 100)
    print('O valor a ser pago é de R$ {}'.format(novoValor))
elif (modoDePagamento == 3):
    novoValor = (valorProduto / 2)
    print('O valor será pago em duas parcelas de R$ {}'.format(novoValor))
else:
    novoValor = (valorProduto + (valorProduto * 20  / 100)) / 3
    print('O valor será pago em três parcelas de R$ {}'.format(novoValor))
