#CALCUlO DE DESCONTO
preco = float(input('Qual é o preço do produto? R$'))
desc = (5 * preco) / 100
total = preco - desc
print(f'O produto que custava {preco},\n'
      f'Na promoção com desconto de 5% vai custar R${total:.2f}')