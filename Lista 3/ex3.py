# ex 2 - aula 4

np1 = float(input("Nota P1: "))
nt1 = float(input("Nota T1: "))
np2 = float(input("Nota P2: "))
nt2 = float(input("Nota T1: "))
media_p1 = (np1 * 0.7) + (nt1 * 0.3) 
media_p2 = (np2 * 0.8) + (nt2 * 0.2)
media_final = (media_p1 * 0.4) + (media_p2 * 0.6)

if media_final >= 7:
    print('Aprovado')
elif media_final <7 and media_final >= 5:
    print('Exame')
else: 
    print('Reprovado')


