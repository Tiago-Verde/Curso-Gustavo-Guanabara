#FAÇA UM PROGRAMA QUE MOSTRE NA TELA UMA CONTAGEM REGRESSIVA PARA O ESTOURO DE FOGOS INDO DE 10 A 0 COM UMA PAUSA DE 1 SEGUNDO ENTRE ELES
import time

print('-=-=-=-=-=-=-=-= ATENÇÃO -=-=-=-=-=-=-=-=-=')    
print('-=-= A contagem regressiva vai começar -=-=')
print('-=-=-=-=-=-=-=-= ATENÇÃO -=-=-=-=-=-=-=-=-=') 
time.sleep(3) 

for c in range (10, -1,-1):
    print(c)
    time.sleep(1)
print('-=' *10)
print('  FELIZ ANO NOVO!!')
print('-=' *10)

