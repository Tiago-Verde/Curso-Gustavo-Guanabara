# DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PROGRESSÃO ARITMETICA. NO FINAL MOSTREA OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO

primeiro = int(input('Qual o primeiro termo: '))
razao = int(input('E a razão: '))
decimo = primeiro + (10 - 1 ) * razao

for c in range(primeiro, decimo + razao, razao):
    print(c)
    
