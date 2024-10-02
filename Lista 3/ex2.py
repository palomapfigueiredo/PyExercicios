'''
7) (Adaptado Boratti, 2007) Faça um programa para calcular o volume de uma esfera de raio 'r'.
O usuário deverá entrar com o raio desejado e deverá ser gerado o retorno do volume.
'''

import math 

r = float(input('Digite o raio: '))
V = (4/3) * math.pi * r ** 3 

print(f'O volume de uma esfera de raio = {r} é {V}')
