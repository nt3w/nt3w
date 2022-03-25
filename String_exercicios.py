# 2. Nome ao contrário em maiúsculas. Faça um programa que permita
# ao usuário digitar o seu nome e em seguida mostre o nome do usuário
# de trás para frente utilizando somente letras maiúsculas. Dica:
# lembre−se que ao informar o nome o usuário pode digitar
# letras maiúsculas ou minúsculas.

# 3. Nome na vertical. Faça um programa que solicite
# o nome do usuário e imprima-o na vertical.

# 4. Nome na vertical em escada. Modifique o programa
# anterior de forma a mostrar o nome em formato de escada.

# 5. Nome na vertical em escada invertida.
# Altere o programa anterior de modo que a escada seja invertida.

nome = str(input('Digite um nome: ')).upper()

# Letras na vertical. Exercício 3 **
for letra in nome:
    print(letra)

# Letras em formado de escada. Exercício 4 **
for letra_escada in range(0, len(nome)+1):
    print(nome[:letra_escada])

print()

# Letras em formato de escada invertida. Exercício 5 **
for letra_escada_inv in range(0, len(nome)+1):
    print(nome[letra_escada_inv:])

# Letras Reversas. Exercício 2 **
nome_rev = ''.join(reversed(nome))

# Palavras reversas. Exercício 2 **
nome_rev_por_palavra = ' '.join(reversed(nome.split()))


print(f'\nNome com letras em maiúsculo: {nome}')
print(f'Nome com letras em maiúsculo invertido por letras: {nome_rev}')
print(f'Nome com letras em maiúsculo'
      f' invertido por palavras: {nome_rev_por_palavra}')
