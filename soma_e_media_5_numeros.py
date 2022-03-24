# Exercício retirado do site https://wiki.python.org.br/EstruturaDeRepeticao
# 8. Faça um programa que leia 5 números
# e informe a soma e a média dos números.


import statistics  # Importado a biblioteca para usar a função "mean(média)".


grupo_num = []  # Lista de números.

while True:
    grupo_num.append(int(input('Digite o número: ')))
    # Irá ser interrompido até que seja fornecido 5 números.
    if len(grupo_num) == 5:
        # Soma dos 5 números fornecido.
        print('A soma dos cinco números digitados é: %d' % sum(grupo_num))
        # Média dos 5 números fornecidos.
        print('Média: %.2f' % statistics.mean(grupo_num))
        break
