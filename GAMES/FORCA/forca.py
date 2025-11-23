import random
import os

# Função para carregar palavras por categoria
def carregar_palavras(categoria):
    palavras = []
    # Arquivo de palavras por categoria (cada linha: PALAVRA)
    nome_arquivo = f"{categoria}.txt"
    caminho_arquivo = os.path.join(os.path.dirname(__file__), nome_arquivo)  # Caminho absoluto do arquivo
    try:
        with open(caminho_arquivo, "r") as arquivo: #abre o arquivo de forma segura
            for linha in arquivo:
                linha = linha.strip() #remove espaços e /n
                if linha != "":
                    palavras.append(linha) #adiciona palavra na lista
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado!")
        return []
    return palavras

# Função principal do jogo
def jogar(): #criar função
    while True:  # LOOP INTERNO: permite jogar novamente
        print("*********************************")
        print("***Bem vindo ao Jogo da FORCA!***") #imprimir uma mensagem
        print("*********************************")

        # Menu de categorias
        while True:
            print("Escolha uma categoria:")
            print("1 - Países")
            print("2 - Frutas")
            print("3 - Animais")
            opcao = input("Digite o número da categoria: ").strip()

            if opcao == "1":
                categoria = "paises"
                break
            elif opcao == "2":
                categoria = "frutas"
                break
            elif opcao == "3":
                categoria = "animais"
                break
            else:
                print("Opção inválida. Digite 1, 2 ou 3.")

        palavras = carregar_palavras(categoria)
        if len(palavras) == 0:
            print("Não há palavras nessa categoria. Voltando ao menu principal.")
            return

        numero = random.randrange(0, len(palavras)) #para buscar a palavra aleatoria na lista
        palavra_secreta = palavras[numero].upper() #upper para deixar as letras maiusculas

        letras_acertadas = ["_" for letra in palavra_secreta] #cada elemento é um caractere de sublinhado ("_")
        letras_erradas = [] #lista para guardar letras erradas

        enforcou = False #True e False são types Bool - Boleanos
        acertou = False
        erros = 0
        pontos = 1000 #pontuação inicial

        print(letras_acertadas)

        while(not enforcou and not acertou): #While - enquanto - Não enforcou e não acertou

            chute = input("Qual a Letra? ") #input é dados ou informações fornecidas
            chute = chute.strip().upper() #strip remove espaços e caracteres, upper deixa maiúscula

            # Impedir que o jogador digite mais de uma letra
            if len(chute) != 1:
                print("Digite apenas UMA letra!")
                continue

            # Evitar que o jogador repita letras já tentadas
            if chute in letras_acertadas or chute in letras_erradas:
                print("Você já tentou essa letra!")
                continue

            if(chute in palavra_secreta): #se a letra estiver na palavra
                index = 0 #é utilizado para encontrar a posição (índice)
                for letra in palavra_secreta: #para cada letra da palavra
                    if(chute == letra): #se a letra chutada for igual à letra da palavra
                        letras_acertadas[index] = letra #substitui o "_" pela letra correta
                    index += 1 # Incrementa o índice para acessar o próximo elemento
                pontos += 50 #pontuação ao acertar letra
            else: #se a letra não estiver na palavra
                erros += 1 #mesma coisa que erros = erros +1
                letras_erradas.append(chute) #adicionar letra errada na lista
                print("Ops, você errou! Faltam {} tentativas.".format(7 - erros))
                desenho(erros) #chama a função que desenha o boneco da forca
                pontos -= 50 #pontuação ao errar letra

            print("Letras erradas:", ", ".join(letras_erradas)) #mostrar letras erradas
            print(letras_acertadas) #mostrar letras acertadas

            enforcou = erros == 7 #Quantidade de tentativas
            acertou = "_" not in letras_acertadas #se o caractere "_" não está dentro das letras acertadas

        if(acertou): #se o jogador acertou
            ganhou()
            print("A palavra era:", palavra_secreta) #mostrar a palavra completa
        else: #se o jogador perdeu
            perdeu(palavra_secreta)

        print(f"Sua pontuação: {pontos}")
        salvar_ranking(pontos) #salvar no arquivo de ranking específico
        mostrar_ranking() #mostrar ranking atualizado

        # Perguntar se o jogador quer jogar novamente
        jogar_novamente = input("Deseja jogar novamente? (S/N): ").upper()
        if jogar_novamente != "S":  # se não for S, sai do loop e volta ao menu principal
            print("Voltando ao menu principal...")
            break

# Função para salvar ranking do jogo da forca
def salvar_ranking(pontos):
    nome = input("Digite seu nome: ").strip()
    caminho_ranking = os.path.join(os.path.dirname(__file__), "ranking_forca.txt")  # Caminho absoluto
    with open(caminho_ranking, "a") as arquivo: #arquivo específico para este jogo
        arquivo.write(f"{nome};{pontos}\n")

# Função para mostrar ranking do jogo da forca
def mostrar_ranking():
    print("\n***** Ranking *****")
    caminho_ranking = os.path.join(os.path.dirname(__file__), "ranking_forca.txt")  # Caminho absoluto
    try:
        with open(caminho_ranking, "r") as arquivo: #arquivo específico para este jogo
            linhas = arquivo.readlines()
            # Ordena por pontos (do maior para menor)
            ranking = []
            for linha in linhas:
                linha = linha.strip()  # remove espaços em branco e \n
                if ";" in linha:  # verifica se a linha está no formato correto
                    nome, pts = linha.split(";")
                    ranking.append((nome, int(pts)))
            ranking.sort(key=lambda x: x[1], reverse=True)
            for i, (nome, pts) in enumerate(ranking[:5]): #mostrar top 5
                print(f"{i+1}. {nome} - {pts}")
    except FileNotFoundError:
        print("Ranking vazio.")

def ganhou(): #função para mensagem de vitória
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")

def perdeu(palavra_secreta): #função para mensagem de derrota
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavra_secreta))
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")

def desenho(erros): #função que desenha o boneco conforme o número de erros
        print("  _______     ")
        print(" |/      |    ")

        if (erros == 1):
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        if (erros == 2):
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")

        if (erros == 3):
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")

        if (erros == 4):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")

        if (erros == 5):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

        if (erros == 6):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")

        if (erros == 7):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")

        print(" |            ")
        print("_|___         ")
        print()

if (__name__ == "__main__"): #verificar se um arquivo está sendo executado como o programa principal
    jogar() #ou se está sendo importado como um módulo em outro arquivo
