alunos = []
escolha = 0

while True:
  nome = str(input('Digite o nome do Aluno: '))
  nota_1 = float(input('Digite a 1º nota do aluno: '))
  nota_2 = float(input('Digite a 2º nota do aluno: '))
  media = (nota_1  + nota_2) / 2
  alunos.append([nome,[nota_1,nota_2],media])
  opc = str(input('Deseja continuar [S/N]?  '))
  if opc in 'Nn':
    break

print("-="*20)
print(f'No. NOME {"MÉDIA":^30}')
print("-"*40)
for al in range(0,len(alunos)):
  print(f'{al}',end='')
  print(f'{alunos[al][0]:^10}',end='')
  print(f'{alunos[al][2]:^25}')

print("-"*40)

while escolha != 999:
  escolha = int(input('Mostrar nota de qual aluno? (999 interrompe): '))
  if escolha == 999:
    break
  else:
    for al in range(0,len(alunos)):
      if escolha == al:
        print(f'Notas de {alunos[al][0]} {alunos[al][1]}')
        print("-"*40)

print('Programa finalizado, até logo!')