'''
8) Faça um programa que calcule a média do aluno, em que:
• Média_P1 = Nota_da_P1 70% + Nota_do_Trabalho 30%.
• Média_P2 = Nota_da_P2 80% + Nota_do_Trabalho 20%.
• Média_Final = Média_P1 40% + Média_P2 60%.
E condição de aprovação da Média_Final:
• Nota >= 7,0 → Aprovado;
• Nota < 7,0 e >= 5,0 → Exame;
• Nota < 5,0 → Reprovado.
Ao final retorne: Média_P1, Média _P2, Média_Final, e a sua respectiva condição. O usuário
terá que entrar com as notas P1, T1, P2 e T2.
'''

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


