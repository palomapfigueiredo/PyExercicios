import math 
 
nA = int(input("Quantos números você deseja na sequência A?")) #pedir ao usuário quantos números ele quer na sequência 

listA = []
listraizA = []
somaA = 0

for i in range(nA):
    seqA = int(input())
    listA.append(seqA) #listar os números escolhidos
    
    if (seqA > 0):
        raizA = math.sqrt(seqA) 
        listraizA.append(raizA) #apresentar as raízes da sequência de números
    else:
        print('Por favor, informe números inteiros!')
    somaA = somaA + seqA #soma dos números da sequência
 
nB = int(input("Quantos números você deseja na sequência B?")) #pedir quantos números terá na outra sequência

listB = []
listraizB = []
somaB = 0

for i in range(nB):
    seqB = int(input())
    listB.append(seqB) #listar números escolhidos

    if (seqB > 0):
        raizB = math.sqrt(seqB)
        listraizB.append(raizB) #apresentar as raízes da sequência B 
    else:
        print("Por favor, informe números inteiros!")
    somaB = somaB + seqB #soma da segunda sequência 

#apresentar todas as informações na tela
print("Sequência A: {}".format(listA))
print("A soma entre eles é {}".format(somaA))
print("As raízes de A são: {}".format(listraizA))  
print("Sequência B: {}".format(listB))
print("A soma entre eles é {}".format(somaB))
print("As raízes de B são: {}".format(listraizB))
