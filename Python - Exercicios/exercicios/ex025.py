# CRIE UM PROGRAMA QUE LEIA UM NOME E DIGA SE ESSE NOME TEM SILVA EM SEU CONTEUDO
nome = str(input('Informe seu nome completo:')).upper().strip()
print('Seu nome possui Silva? {}'.format('SILVA' in nome))
