# REFAÇA O DESAFIO NUMERO 35 MAS MOSTRE EM SEU RESULTADO SE O TRIANGULO É
# EQUILATERO - TODOS OA LADOS IGUAIS
# ISOSCELES - DOIS LADOS IGUAIS
# ESCALENO - NENHUM LADO IGUAL

lado1 = float(input('Informe o valor do primeiro lado:'))
lado2 = float(input('Informe o valor do segundo lado:'))
lado3 = float(input('Informe o valor do terceiro lado:'))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado2 + lado1:
    print('Pode ser formado um triangulo')
else:
    print('Não é possivel formar um tringulo')

if (lado1 == lado2) and (lado2 == lado3):
    print('Temos um triangulo do tipo equilatero')
elif (lado1 == lado2) or (lado1 == lado3) or (lado2 == lado3):
    print('Temos um tringulo do tipo isosceles')
else:
    print('Temos um triangulo do tipo escaleno')

