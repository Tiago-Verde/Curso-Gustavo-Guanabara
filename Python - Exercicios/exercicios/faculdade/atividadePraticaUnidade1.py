# Desenvolva um algoritmo que seja capaz de receber do usuário via teclado a número que corresponde a uma idade (um valor numérico inteiro), na sequência o algoritmo deverá 
# verificar se a idade fornecida é igual ou maior que 21, caso seja, deverá exibir a mensagem “Maior de idade, acesso liberado.”, 
# caso contrário deverá exibir a mensagem “Acesso negado, menor de idade.”.


idade = int(input('Informe a sua idade: '))
if  idade >= 21:
    print('Maior de idade, acesso liberado')
else:
    print('Acesso negado, menor de idade')

    