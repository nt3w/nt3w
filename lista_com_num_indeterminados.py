# Exercício retirado do site https://wiki.python.org.br/ExerciciosListas
# 15 Faça um programa que leia um número indeterminado de valores,
# correspondentes a notas, encerrando a entrada de dados quando
# for informado um valor igual a -1 (que não deve ser armazenado).
# Após esta entrada de dados, faça:

notas = []

while True:
    entrada = input('Digite a nota: ')
    if entrada == '-1':
        break
    notas.append(float(entrada))

# a) Mostre a quantidade de valores que foram lidos;
tamanho = len(notas)
print(f'\nFoi contabilizado {tamanho} notas\n')

# b) Exiba todos os valores na ordem em que foram informados,
#    um ao lado do outro;
print(' '.join([str(nota) for nota in notas]))
print('\n')

# c) Exiba todos os valores na ordem inversa à que foram informados,
#    um abaixo do outro;
notas.reverse()

for nota in notas:
    print(nota)

# d) Calcule e mostre a soma dos valores;
soma = sum(notas)
print(f'\nNotas somadas: {soma}')

# e) Calcule e mostre a média dos valores;
media = soma / tamanho
print(f'\nA Média das notas é {media}')


# f) Calcule e mostre a quantidade de valores acima da média calculada;

print('Notas acima da média: ')
print(' '.join([str(nota) for nota in notas if nota > media]))

# g) Calcule e mostre a quantidade de valores abaixo de sete;

print('\nNotas abaixo da média 7: ')
print(' '.join([str(nota) for nota in notas if nota < 7]))

# h) Encerre o programa com uma mensagem;
print('\nFIM!')
