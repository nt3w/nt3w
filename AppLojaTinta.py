# Faça um Programa para uma loja de tintas.
# O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
# e que a tinta é vendida em latas de 18 litros
# que custam R$ 80, 00 ou em galões de 3, 6 litros  que custam R$ 25, 00.
# Informe ao usuário as quantidades de tinta a serem compradas
# e os respectivos preços em 3 situações:
# comprar apenas latas de 18 litros
# comprar apenas galões de 3, 6 litros
# misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10 % de folga e sempre arredonde os valores para cima
# isto é, considere latas cheias.

import math


class Efc:                # **** Off Exercício! ****
    VER = '\033[91m'   # **** Off Exercício! ****
    FIM = '\033[0m'      # **** Off Exercício! ****
    NGT = '\033[1m'


info = float(input('Quantos m² tem a área a ser pintada: '))

m2_pintura = info * 1.1  # +10%
#            metro² informado
litro_m2 = 6  # 1 litro de tinta pinta 6m²
tinta_m2 = m2_pintura / litro_m2

latas = 18  # litros
valor_latas = 80

qtd_latas = math.ceil(tinta_m2 / latas)

preco_latas = qtd_latas * valor_latas  # Preço total para a
# ... quantidade necessária de lata.

print(f'Para pintar a área de {Efc.VER}{Efc.NGT}{info}m²{Efc.FIM} será'
      f' necessário {Efc.VER}{Efc.NGT}{qtd_latas} lata(as){Efc.FIM},'
      f' com preço total de R$ {Efc.VER}{Efc.NGT}{preco_latas}{Efc.FIM}.')

galao = 3.6  # litros
valor_galao = 25

qtd_galao = math.ceil(tinta_m2 / galao)

preco_galao = qtd_galao * valor_galao  # Preço total para a
# ... quantidade necessária de lata.

print(f'Para pintar a área de {Efc.VER}{Efc.NGT}{info}m²{Efc.FIM} será'
      f' necessário {Efc.VER}{Efc.NGT}{qtd_galao} galão(ões){Efc.FIM},'
      f' com preço total de R$ {Efc.VER}{Efc.NGT}{preco_galao}{Efc.FIM}.')

# Otimização Latas + Galões

num_resto_lata = math.floor(tinta_m2 / latas)
lata_resto_preco = num_resto_lata * 80

resto = tinta_m2 % latas

num_resto_galao = math.ceil(resto % galao)
galao_resto_preco = num_resto_galao * 25

resto_total = lata_resto_preco + galao_resto_preco

print(f'Para pintar a área de {Efc.VER}{Efc.NGT}{info}m²{Efc.FIM} será'
      f' necessário {Efc.VER}{Efc.NGT}{num_resto_lata} lata(as){Efc.FIM},'
      f' mais {Efc.VER}{Efc.NGT}{num_resto_galao} galão(ões){Efc.FIM},'
      f' com preço total de R$ {Efc.VER}{Efc.NGT}{resto_total}{Efc.FIM}.')
