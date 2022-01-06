# FAÇA UM ALGORITMO QUE LEIA O SALARIO DE UM FUNCIONÁRIO E APRESENTE NA TELA ESSE SALÁRIO COM 15 DE AUMENTO
salario = float(input('Qual o valor do salario do colaborador: '))
aumento = salario + ( salario * 15/100)
print('O salario com 15% de  aumento é de {}'.format(aumento))