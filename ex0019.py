import random
aluno1 = input('Informe o nome do primeio aluno: ')
aluno2 = input('Informe o nome do segundo aluno: ')
aluno3 = input('Informe o nome do terceiro aluno: ')
aluno4 = input('infomre o nome do quarto aluno: ')

list = [aluno1, aluno2, aluno3, aluno4]
sortei = random.choice(list)
print(f'O aluno que vai apagar o quadro é {random.choice(list)}')
