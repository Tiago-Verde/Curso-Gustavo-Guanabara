# FAÇA UM PROGRAMA QUE PERGUNTE O SALARIO DO COLABORAR E MOSTRE O VALOR DO AUMENTO
# PARA SALARIOS SUPERIORES A R$ 1250,00 CALCULE UM AUMENTO DE 10%
# PARA SALARIOS INFERIORES O AUMENTO É DE 15%

valorSalario = float(input('Qual o valor de seu salário? '))
if valorSalario <= 1250:
    novoSalario = ((valorSalario * 15)/100) + valorSalario
    print('Seu novo salario é de R$ {}'.format(novoSalario))
else:
    novoSalario = ((valorSalario * 10)/100) + valorSalario
    print('Seu novo salario é de R$ {}'.format(novoSalario))
print('Não gaste tudo de uma só vez')
