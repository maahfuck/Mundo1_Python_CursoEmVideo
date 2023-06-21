frase = str(input('Digite uma frase: ')).strip()
print(f"""A letra A aparece: {frase.upper().count('A')} vezes
A primeira letra A apareceu na posição {frase.upper().find('A')+1}
A última letra A apareceu na posição {frase.rfind('a')+1}""")
