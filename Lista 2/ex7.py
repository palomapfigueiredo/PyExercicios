sexo = str(input("Sexo (responda 'M' para masculino e 'F' para feminino):"))
idade = int(input("Idade:"))
tempo = int(input("Qual seu tempo de contribuição para INSS? "))

if sexo == 'M':  #verifica se o homem pode se aponsentar ou não
    if idade >= 65 and tempo >= 10:
        print('Aposentável.')
    elif idade >= 63  and tempo >=15:
        print('Aposentável.')
    else:
        print('Não aposentável.')
elif sexo == 'F': #verifica as condições da mulher para possível aposentadoria 
    if idade >= 63 and tempo >= 10:
        print('Aposentável.')
    elif idade >= 61  and tempo >=15:
        print('Aposentável.')
    else:
        print('Não aposentável.')
else: 
    print('[ERRO] Você deve responder os itens conforme solicitado.')