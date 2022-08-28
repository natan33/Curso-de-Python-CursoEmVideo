from random import sample

n1 = str(input('Primeiro Aluno: '))
n2 = str(input('Segundo Aluno: '))
n3 = str(input('Terceiro Aluno: '))
n4 = str(input('Quarto Aluno: '))
list = [n1, n2, n3, n4]

print('A ordem de apresentação será')
print(sample(list, 4))
