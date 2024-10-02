'''
9) Desenvolva um programa para a equação: S = S0 + v.t, onde:
S = espaço final; S0 = espaço inicial; V = velocidade; t = tempo (instante).
Considere o espaço inicial igual 0, e a velocidade for 50:
O programa deve solicitar o tempo, e ao final, retornar o espaço percorrido.
'''

tempo = float(input('Tempo: ')) 
S_inicial = 0 
vel = 50 

S_final = S_inicial + (vel * tempo)

print(f"O espaço percorrido foi de {S_final:.0f} metros.")