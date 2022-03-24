# Supondo que a população de um país A seja da ordem de 80000 habitantes
# com uma taxa anual de crescimento de 3% e que a população de B seja 200000
# habitantes com uma taxa de crescimento de 1.5%. Faça um programa
# que calcule e escreva o número de anos necessários para que a população
# do país A ultrapasse ou iguale a população do país B,
# mantidas as taxas de crescimento.

Pais_A = 80000   # População Pais A
Taxa_A = 0.03    # Taxa de crescimento populacional Pais A - 3%
Pais_B = 200000  # População Pais B
Taxa_B = 0.015   # Taxa de crescimento populacional Pais B - 1,5%
Tempo = 0

while True:
    Pais_A += (Pais_A * Taxa_A)
    Pais_B += (Pais_B * Taxa_B)
    Tempo += 1
    if Pais_A > Pais_B:
        Dif = int(Pais_A - Pais_B)

        print(f'A população do Pais A ultrapassou a população do Pais B'
              f' em {Dif} habitantes e em um total de {Tempo} anos!')
        print('Populaçao %d' % (Pais_A))
        print('População %d' % (Pais_B))
        break
