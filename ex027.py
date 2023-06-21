#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input(f'Digite seu nome: ')).strip().title().split()
print(f'Seu primeiro nome é {nome[0]} e seu último nome é {(nome[1])}.')
print('Olá {} {}! '.format(nome[0], nome[len(nome)-1])) # -1 pq o python conta a posição 0