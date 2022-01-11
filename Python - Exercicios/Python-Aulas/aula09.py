frase = 'Curso em video Python'
print(frase)
print(frase[3:13])
print(frase[:13])
print(frase[13:])
print(frase[1:15])
print(frase[1::2])

print("""Eu estou testando um texto maior que pode ter quebra de linha
e quero saber se o print irá acontecer normalmente em. Então imagine que teremos aqui varias linhas

corinthians 2 x 0 flamengo

Santos 0 x 0 Palmeiras

Paulista FC 2 x 1 Atletico Mineiro  """)

print(frase.count('o'))
print(frase.upper().count('O'))

print(len(frase))

print(frase.replace('Curso', 'Treinamento'))

print(frase.split())

lista = frase.split()

print(lista[0])
print(lista[2])
print(lista[2][3])