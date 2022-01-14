# FAÇA UM PROGRAMA QUE PERGUNTE A DISTANCIA DE UMA VIAGEM EM KM E CALCULE O PREÇO DA PASSAGEM COBRANDO R$ 0,50 POR KM PARA VIAGENS 
# DE ATÉ 200KM E R$ 0,45 PARA VIAGENS MAIS LONGAS

distancia = float(input('Quantos quilometros você vai viajar?'))
if distancia <= 200:
    passagem = distancia * 0.50
else:
    passagem = distancia * 0.45
print('A sua passagem ficou em R$ {}'.format(passagem))