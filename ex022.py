nome = str(input('Digite seu nome: ')).strip()
print('_'*100)
print('Analisando seus dados...')

print(f'Seu nome em maiúsculas é: {nome.upper()}')
print(f'Seu nome em minúsculas é: {nome.lower()}')
print(f'O seu nome tem: {len(nome)- nome.count(" ")} letras')
#print(f'Seu primeiro nome tem: {len(nome.split()[0])}')
print(f'Seu primeiro nome tem: {nome.find(" ")}')
