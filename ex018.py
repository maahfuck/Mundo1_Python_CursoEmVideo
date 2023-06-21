from math import radians, cos, sin, tan
ang = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ang))
print(f'O ângulo de {ang} tem o SENO de {seno:.2f}')
cos = cos(radians(ang))
print(f'O ângulo de {ang} tem o COSSENO de {cos:.2f}')
tan = tan(radians(ang))
print(f'O ângulo de {ang} tem o TANGENTE de {tan:.2f}')