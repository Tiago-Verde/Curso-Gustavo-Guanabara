a = int(input('Primeiro Valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor'))

if a > b and a > c:
    print('O primeiro valor é o maior valor: {}'.format(a))
elif b > a and b > c:
    print('Osegundo valor é o maior valor: {}'.format(b))
else:
    print('O terceiro valor é o maior valor: {}'.format(c))
print('Fim do programa')