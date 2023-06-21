aluguel = int(input('Quantos dias alugado? '))
km = float(input('Quantos KM percorridos? '))
total = aluguel * 60 + km * 0.15
print(f'Você pagará um valor de {total}')
