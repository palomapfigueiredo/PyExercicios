import math

a = float(input('Insira o coeficiente A:'))
b = float(input('Insira o coeficiente B:'))
c = float(input('Insira o coeficiente C:'))

#coeficiente a != 0
if a == 0:
    print("O coeficiente 'a' não pode ser zero em uma equação quadrática!")

#Para determinar o vértice da parábola
xv = -b / (2 ** a)

#Para substituir o xv na função para descobrir o valor extermo
fxv = a * (xv ** 2) + b * xv + c

if a > 0:
    v_extremo = 'mínimo'
else: 
    v_extremo = 'máximo'

print(f"O vértice da parábola está em x = {xv:.2f}")
print(f"O valor de f(x) no vértice é {fxv:.2f}, que é um {v_extremo} da função.")

