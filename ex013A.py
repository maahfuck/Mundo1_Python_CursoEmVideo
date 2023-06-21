val = float(input('Qual é o valor do produto? R$: '))
print(f'Se o pagamento for a vista ficará no preço de: {val - (val*10/100):.2f}')
print(f'E se o produto for a prazo ficará no valor de: {val + (val*8/100):.2f}')