num = int(input('Informe os números: '))
print('_'*100)
print(f'Analisando seus dados os números {num}')

print(f"""Unidade: {num // 1 % 10}
Dezena: {num // 10 % 10}
Cetena: {num // 100 % 10}
Milhar: {num // 1000 % 10}""")

print('_'*100)

print('FIM')


