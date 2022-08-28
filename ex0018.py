from math import cos, sin, tan, radians
ang = (float(input('Digite o Ângulo que você deseja: ')))
r = radians(ang)
c = cos(r)
s = sin(r)
t = tan(r)

print(f'O angulo de {ang} tem cosseno de {cos(r):.2f}\n'
      f'O seno de {sin(r):.2f}\n'
      f'E o tangente de {tan(r):.2f}')


