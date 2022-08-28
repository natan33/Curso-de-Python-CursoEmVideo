nome = str(input('Nome completo:'))
print(f'Seu nome MAIÚSCULO {nome.upper()}')
print(f'Seu nome minúsculo {nome.lower()}')
esp = (nome.replace(' ',''))
print(f'Seu nome tem ao todo {len(esp)} letras')
print(f'Seu primeiro nome é {nome.split()[0]} e ele tem {len(nome.split()[0])} letras')



