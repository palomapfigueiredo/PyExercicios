ano = int(input('Digite um ano:')) #pedir o ano
if  ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0: #verifica se o ano for divível por 400 ou por 4 e o resto de 100 for diferente de 0, ele é bissexto
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} não é bissexto.')


