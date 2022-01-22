# CRIE UM PROGRAMA QUE  FAÇA ALEITURA DO PESO DO USUARIO E FAÇA O CALCULO DO IMC
# ABAIXO DE 18.5 - ABAIXO DO PESO
# ENTRE 18.5 E 25.0 - PESO IDEAL
# 25.0 A 30.0 SOBREPESO
# 30.0 A 40.0 OBESIDADE
# ACIMA DE 40.0 OBESIDADE MORBIDA

peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso / (altura * altura)

print('O seu IMC é de {}'.format(imc))

if imc < 18.5:
    print('Você esta abaixo do peso')
elif (imc >= 18.5) and (imc <= 25.0):
    print('Você tem o peso ideal')
elif (imc > 25.0) and (imc <= 30.0):
    print('Você tem sobrepeso')
elif (imc > 30.0) and (imc <= 40.0):
    print('Você possui obesidade')
else:
    print('Você tem obesidade morbida')