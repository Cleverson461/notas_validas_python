# Escreva um programa que receba notas de um aluno(0 - 10), caso a nota digitada esteja fora desse intervalo peça para o professor digitar novamente

nota = float(input('Digite a nota do aluno: '))

while nota < 0 or nota > 10:
  print('Nota inválida, digite novamente')
  nota = float(input('Digite uma nota valida: '))

print(f'A nota do aluno é: {nota}')
  