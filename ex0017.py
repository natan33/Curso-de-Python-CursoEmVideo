#Exercicio 17 > Buscar a hipotenusa
from math import hypot
#hypot é a função do modulo math para saber a hipotenusa
cto = float(input('Informe o cateto oposto: '))
ctad = float(input('Informe o cateto adjacente: '))

print(f'A soma dos catetos é igual o comprimento da hipotenusa {hypot(cto,ctad)}')
