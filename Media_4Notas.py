# Exércicio: Recebe quatro notas e retorna média e APROVADO/RECUPERAÇÃO/REPROVADO


nota = float(input('Digite Nota 1:'))
nota2 = float(input('Digite Nota 2:'))
nota3 = float(input('Digite Nota 3:'))
nota4 = float(input('Digite Nota 4:'))

media = (nota + nota2 + nota3 + nota4) / 4

if media == 10:
    print(f'O aluno obteve uma média de {media}, e está APROVADO sem destinção!')
elif media >= 7 and media <= 9.99:
    print(f'O aluno obteve uma média de {media}, e está APROVADO!')
elif media >= 5.50 and media <= 6.99:
    print(f'O aluno obteve uma média de {media}, e está EM RECUPERAÇÃO!')
else:
    print(f'O aluno obteve uma média de {media}, e está REPROVADO')


print('Fim!')
