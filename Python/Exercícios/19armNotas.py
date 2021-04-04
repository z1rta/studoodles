print('-'*30)
print('Armazenamento de Notas')
print('-'*30)
somaN1 = 0
somaN2 = 0
n1 = 0
n2 = 0

print('~'*30)
print('VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS ÍMPARES')
print('~'*30)
for x in range(1, 50, 2):
    n1 = input('Por favor, insira a nota do aluno {}: '.format(x))
    somaN1 = int(somaN1) + int(n1)

print('\n')
print('~'*30)
print('VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES')
print('~'*30)
for x in range(2, 50, 2):
    n2 = input('Por favor, insira a nota do aluno {}: '.format(x))
    somaN2 = int(somaN2) + int(n2)

mediaN1 = somaN1 / 25
mediaN2 = somaN2 / 25
print('A média dos alunos ímpares é {:.2f}'.format(mediaN1))
print('A média dos alunos pares é {:.2f}'.format(mediaN2))

if mediaN1 > mediaN2:
    print('A média da turma ímpar é maior.')
else:
    print('A média da turma par é maior.')
