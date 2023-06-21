#Escreva um programa que leia a velocidade de um carro
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai curtar 7 reais por cada Km acima do limite

from random import randint
from time import sleep

vel_carro = randint (10,180)
print('Seu carro passou no radar 🚗...')
sleep(0.5)

multa = (vel_carro - 100)*7
if vel_carro <= 100:
    print(f'Você está a {vel_carro}Km/h \nContinue assim...')
else:
    print(f"""Você está a {vel_carro}Km/h e foi multado
você deve pagar uma multa de R${multa:.2f}
Tenha um bom dia e dirija com segurança""")


