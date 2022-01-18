# FAÇA UM ALGORITMO QUE LEIA O SALARIO DE UM FUNCIONÁRIO E APRESENTE NA TELA ESSE SALÁRIO COM 30 DE AUMENTO
salario = float(input('Qual o valor do salario do colaborador: '))
aumento = salario + ( salario * 30/100)
print('O salario com 30% de  aumento é de {}'.format(aumento))