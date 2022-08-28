#Pintando Parede
larg = float(input('Qual é a larguda da parede'))
alt = float(input('Altura da parede'))
area = alt * larg

print(f'Sua parede tem a dimensão de {larg}x{alt} e sua area de {area}m²')
tinta = area / 2
print(f'Para pintar sua parede, você precisará de  {tinta}l de tinta')
