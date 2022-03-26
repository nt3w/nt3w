# 8. Faça um Programa que pergunte quanto você ganha por hora e
# o número de horas trabalhadas no mês. Calcule e mostre
# o total do seu salário no referido mês.

valor_hr = float(input('Valor da Hora Trabalhada: '))
dias = float(input('Digite quantos dias trabalhados: '))
quantidade_hr = float(
    input('Digte a quantidade de Horas Trabalhadas por Dia: '))


salario = quantidade_hr * valor_hr * dias


imp_renda = 0.11
inss = 0.08
sindicato = 0.05

imp_geral = imp_renda + inss + sindicato

deducao = salario * imp_geral
salario_final = salario - deducao

print(f'\nCarga Horária total: {quantidade_hr * dias} horas/mês\n')
print(f'+ Salário Bruto: R$ {salario}\n')
print(f'Deduções: \n'
      f' - IR: {imp_renda*100}% = R$ {salario * imp_renda}'
      f'\n - INSS: {inss*100}% = R$ {salario * inss}'
      f'\n - Sindicato: {sindicato*100}% = R$ {salario * sindicato}')
print(' - TOTAL DEDUZIDO: R$ %.2f' % deducao)
print('\n= Salário Líquido: R$ %.2f' % salario_final)
