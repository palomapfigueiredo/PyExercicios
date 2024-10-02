'''
6) Faça um algoritmo que leia um caractere ‘F’ ou ‘C’, que indica se o próximo valor
corresponde à temperatura em Fahrenheit ou Celsius. Em seguida, o programa deve ler o
valor da temperatura e então imprimir o valor correspondente à temperatura na outra
unidade de medida. Observação: (C = 5/9 × (F − 32)).
'''

unidade = input("Digite 'F' para Fahrenheit ou 'C' para Celsius: ") 
 
if unidade == "C":
    temperatura = float(input("Digite a temperatura em Fahrenheit: ")) 
    c = 5/9 * (temperatura - 32) #transforma a temperatura em Fahrenheit para Celsius 
    print(f'{temperatura}°F equivale a {c:.2f}°C.')
elif unidade == "F":
    temperatura = float(input("Digite a temperatura em Celsius: "))
    f = (temperatura * 9/5) + 32 #transforma a temperatura em Celsius para Fahrenheit 
    print(f'{temperatura}°C equivale a {f:.2f}°F.')
else: 
    print("ERRO! Por favor, digite 'F' para Fahrenheit ou 'C' para Celsius") 


