'''
5) Considere a equação quadrática ax2 + bx + c = 0, onde a, b, c ∈ R e a ≠ 0.
Desenvolva um programa que, dados os coeficientes a, b e c fornecidos pelo usuário,
determine:

Se Δ > 0, a equação possui duas raízes reais e distintas,
Se Δ = 0, a equação possui uma única raiz real,
Se Δ < 0, a equação não possui raízes reais.

Máximo ou Mínimo da Função Quadrática:

Determine o vértice da parábola representada pela função quadrática f(x) = ax2 + bx + c. O
valor de x que corresponde ao vértice é dado por:

xv = −b / (2a)

Substitua xv na função f(x) para calcular o valor extremo:
f(xv) = a(−b / (2a))2 + b(−b / (2a)) + c;
Se a > 0, f(xv) é o mínimo da função.
Se a < 0, f(xv) é o máximo da função.
'''

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

