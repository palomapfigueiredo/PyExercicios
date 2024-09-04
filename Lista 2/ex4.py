n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1 > n2 and n1 > n3: #verificar se o primeiro número é o maior
    print(f"O número {n1} é o maior entre eles.")
elif n2 > n1  and n2 > n3: #verificar se o segundo número é o maior
    print(f"O número {n2} é o maior entre eles.")
elif n3 > n1  and n3 > n2: #verificar se o terceiro número é o maior
    print(f"O número {n3} é o maior entre eles.")

if n1 < n2 and n1 < n3: #verificar se o primeiro número é o menor
    print(f"O número {n1} é o menor entre eles.")
elif n2 < n1  and n2 < n3: #verificar se o segundo número é o menor
    print(f"O número {n2} é o menor entre eles.")
elif n3 < n1 and n3 < n2: #verificar se o terceiro número é o menor
    print(f"O número {n3} é o menor entre eles.")
else:
    print('Os números são iguais. ') #verifica se são todos iguais 