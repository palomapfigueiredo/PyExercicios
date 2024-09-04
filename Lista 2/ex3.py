numero = int(input('Digite um número inteiro:'))

divisores = 0 #inicia-se com 0 divisores 

for i in range(1, numero +1 ): #começa em 1 e atribui a i +1
    if numero % i== 0: #se o número dividido por i restar 0 significa que i é um divisor de número
        divisores += 1 #quando i for divisível acrescentamos +1 na variável divisores 

if divisores == 2: #para um número ser primo, deve ter dois divisores, 1 e ele mesmo, ou seja, caso o números de divisores dê diferente de 2, o número não será primo
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")


