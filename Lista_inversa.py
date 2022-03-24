# Exercício retirado do site https://wiki.python.org.br/ExerciciosListas
# 2. Faça um Programa que leia um vetor de 10 números
# reais e mostre-os na ordem inversa.



Lista = []  # Lista onde será armazenado os números fornecidos.

for _ in range(10):  # Quantidades de números a ser fornecido para a lista.
    num = float(input('Digite um número: '))
    Lista.append(num)


print(Lista[::-1])  # Lista em tela apresentando ordem inversa.


# Extra
# Também séria possível ultilizar o seguinte código comentado:

'''
for _ in range(10):
    num = float(input('Digite um número: '))
    Lista.append(num)
    Lista.reverse()

print(Lista)
'''
