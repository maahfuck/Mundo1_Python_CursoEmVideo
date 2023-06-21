from random import randint
from time import sleep

print('-'*24, '*'*1,'-'*25)
titulo = ('Jogo de Adivinhar')
print(f'{titulo:^56}')
print('-'*24, '*'*1,'-'*25)
num = randint(0,10)
resp = int(input('Me diga um número de 0 a 10: '))

print('Processando', end=''),
sleep(0.5)
print(' .', end='')
sleep(0.5)
print(' .', end='')
sleep(0.5)
print(' .\n')
sleep(0.5)

print('-'*24, '*'*1,'-'*25)

if num == resp:
    print(f'PARABÉNS!!! Você Acertou! Eu escolhi o número: {num}')
else:
    print(f'Err, você errou, eu escolhi o número: {num}')




