nome = str(input('Qual o seu nome???')).upper()
if nome == 'TIAGO':
    print("Uau, que nome lindo")
elif nome == 'ANA':
    print('Você tem o nome da minha sobrinha')
elif nome == 'JANDIRA':
    print('Taaaarde Jandira')
else:
    print('Esse nome é bem normal')
print('Tenha um bom dia {}, até a proxima'.format(nome))