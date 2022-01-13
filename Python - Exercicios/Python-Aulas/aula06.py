# FUNÇÃO TYPE IDENTIFICA QUAL O TIPO DA VARIAVEL
n1 = input("Digite um valor: ")
print(type(n1))

# DEVO INFORMAR O TIPO PRIMITIVO DA VARIAVEL PARA QUE EU POSSA USALA CORRETAMENTE
n2 = int(input("Digite um valor: "))
print(type(n2))

# PRINT SEM A UTILIZAÇÃO DO .FORMAT E CONCATENAÇÃO SIMPLES
n3 = int(input("Informe um numero para realizarmos a soma: "))
n4 = int(input('Informe o segundo valor: '))
soma = (n3+n4)
print('A soma entre ', n3, " e ", n4, " é de ", soma)

# PRINT UTILIZANDO A FUNÇÃO .FORMAT
n4 = int(input('Informe um valor para realizarmos a segunda soma: '))
n5 = int(input('Informe o segundo valor: '))
soma2 = (n4+n5)
print('A soma de {} e {} é de {}'.format(n4, n5, soma2))


