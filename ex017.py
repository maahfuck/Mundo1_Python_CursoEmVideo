import math
catetoopo = float(input('Comprimento do cateto oposto: '))
catetoadj = float(input('Comprimento do cateto adjacente: '))
#result = (catetoopo**2 + catetoadj**2) **(1/2)
#print(f'A hipotenusa vai medir {result:.2f}')
result = math.hypot(catetoopo, catetoadj)
print(f'A hipotenusa vai medir {result}')