#Criar o tabuleiro 3x3
tabuleiro = [
    [' ', ' ', ' '],  
    [' ', ' ', ' '],  
    [' ', ' ', ' ']
]
jogador = "X"

while True:
    #Exibir o tabuleiro
    for linha in tabuleiro:
        print(f" {linha[0]} | {linha[1]} | {linha[2]} ")
        print("---|---|---")

    #Solicitar jogada do jogador
    print(f"Jogador {jogador}, é sua vez!")
    linha = int(input("Escolha a linha (1-3): ")) - 1
    coluna = int(input("Escolha a coluna (1-3): ")) - 1
    
    #Verificar se a posição está livre
    if tabuleiro[linha][coluna] != " ":
        print("Essa posição já está ocupada! Tente novamente.")
        continue
    
    #Fazer a jogada
    tabuleiro[linha][coluna] = jogador

    #Verificar se o jogador atual venceu
    if (tabuleiro[0][0] == tabuleiro[0][1] == tabuleiro[0][2] == jogador or  #Linhas
        tabuleiro[1][0] == tabuleiro[1][1] == tabuleiro[1][2] == jogador or
        tabuleiro[2][0] == tabuleiro[2][1] == tabuleiro[2][2] == jogador or
        tabuleiro[0][0] == tabuleiro[1][0] == tabuleiro[2][0] == jogador or  #Colunas
        tabuleiro[0][1] == tabuleiro[1][1] == tabuleiro[2][1] == jogador or
        tabuleiro[0][2] == tabuleiro[1][2] == tabuleiro[2][2] == jogador or
        tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador or  #Diagonais
        tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador):
        for linha in tabuleiro:
            print(f" {linha[0]} | {linha[1]} | {linha[2]} ")
            print("---|---|---")
        print(f"Jogador {jogador} venceu!")
        break

    #Verificar se o tabuleiro está cheio (empate)
    if all([posição != " " for linha in tabuleiro for posição in linha]):
        for linha in tabuleiro:
            print(f" {linha[0]} | {linha[1]} | {linha[2]} ")
            print("---|---|---")
        print("O jogo terminou em empate!")
        break

    #Alternar jogadores
    jogador = "O" if jogador == "X" else "X"
