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


