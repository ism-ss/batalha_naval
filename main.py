import random
#Variaveis
acertos = 0
erros = 0
tiros = 0
#Funções
def mostrar_menu():
    print("\n--- MENU ---")
    print("1 - Mostrar Tabuleiro")
    print("2 - Dar Tiro")

def criar_tabuleiro():
    tabuleiro = []

    i = 0
    while i <= 9:
        tabuleiro.append([0,0,0,0,0,0,0,0,0,0])
        i += 1

    return tabuleiro

def mostrar_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        for posicao in linha:

            if posicao == "X":
                print("X", end=" ")

            elif posicao == "O":
                print("O", end=" ")

            else:
                print("~", end=" ")

        print()

def posicionar_navios(tabuleiro):
    for i in range(3):
        linha = random.randint(0, 9)
        coluna = random.randint(0, 7)

        tabuleiro[linha][coluna] = 1
        tabuleiro[linha][coluna + 1] = 1
        tabuleiro[linha][coluna + 2] = 1
    for i in range(2):
        linha = random.randint(0, 9)
        coluna = random.randint(0, 7)

        tabuleiro[linha][coluna] = 1
        tabuleiro[linha][coluna + 1] = 1
    for i in range(1):
        linha = random.randint(0, 9)
        coluna = random.randint(0, 6)

        tabuleiro[linha][coluna] = 1
        tabuleiro[linha][coluna + 1] = 1
        tabuleiro[linha][coluna + 2] = 1 
        tabuleiro[linha][coluna + 3] = 1 

def dar_tiro(tabuleiro, linha, coluna):
    global acertos, erros, tiros
    if tabuleiro[linha][coluna] == 1:
        print("Acertou!")
        tabuleiro[linha][coluna] = "X"
        acertos = acertos + 1
        tiros = tiros + 1
    elif tabuleiro[linha][coluna] == "X" or tabuleiro[linha][coluna] == "O":
        print("Tiro Repetido")
    else:
        print("Errou!")
        tabuleiro[linha][coluna] = "O"
        erros = erros + 1
        tiros = tiros + 1

def acabou(tabuleiro):
    for linha in tabuleiro:
        for posicao in linha:
            if posicao == 1:
                return False

    return True

tabuleiro = criar_tabuleiro()
posicionar_navios(tabuleiro)

input("Aperte enter para começar a Batalha Naval")

print("")
print("Tabuleiro gerado com sucesso!")
print("")
print("Navios posicionados com sucesso")

while True:

    mostrar_menu()
    opcao = input("Escolha: ")

    if opcao == "1":
        mostrar_tabuleiro(tabuleiro)

    elif opcao == "2":

        linha = int(input("Digite a linha do tabuleiro onde deseja atirar: "))

        if linha == -1:
            print("\nJogo encerrado!")
            print("Tiros:", tiros)
            print("Acertos:", acertos)
            print("Erros:", erros)

            if tiros > 0:
                print("Precisão:", (acertos / tiros) * 100, "%")

            break

        if linha < 0 or linha > 9:
            print("Linha inválida!")
            continue

        coluna = int(input("Digite a coluna do tabuleiro onde deseja atirar: "))

        if coluna < 0 or coluna > 9:
            print("Coluna inválida!")
            continue

        dar_tiro(tabuleiro, linha, coluna)
        mostrar_tabuleiro(tabuleiro)

        if acabou(tabuleiro):
            print("\nVocê venceu!")
            print("")

            print("Tiros:", tiros)
            print("Acertos:", acertos)
            print("Erros:", erros)

            if tiros > 0:
                print("Precisão:", (acertos / tiros) * 100, "%")

            break

    else:
        print("Opção inválida")