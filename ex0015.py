#Aluguel de Carros
dias_alg = (int(input('Quantos dias Alugados? ')))
km_rods = (float(input('Quantos Km rodados? ')))
total = (60 * dias_alg) + (0.15 * km_rods)

print(f'total a pagar {total:.2f}')

