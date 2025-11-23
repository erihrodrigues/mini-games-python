import random  #Importa o módulo RANDOM, que permite gerar números aleatórios
import os  #Importa o módulo OS para lidar com caminhos de arquivos

#Função para carregar o ranking do arquivo
def carregar_ranking():
    try:
        # Caminho do arquivo "ranking.txt" relativo a este script
        caminho_ranking = os.path.join(os.path.dirname(__file__), "ranking.txt")

        #Tenta abrir o arquivo "ranking.txt" no modo leitura
        #Abre o arquivo "ranking.txt" no modo leitura ("r").
        #O WITH garante que o arquivo será fechado automaticamente quando o bloco terminar
        #mesmo que aconteça algum erro. A variável ARQUIVO representa o arquivo aberto dentro do bloco.
        with open(caminho_ranking, "r") as arquivo:
            linhas = arquivo.readlines()  #Lê todas as linhas do arquivo
            ranking = []  #Lista vazia para armazenar os jogadores carregados

            #Percorre cada linha do ranking
            for linha in linhas:
                # Separa nome e pontos usando ';' como separador
                nome, pontos = linha.strip().split(";")
                ranking.append((nome, int(pontos)))  #Salva como tupla (nome, pontos)

            return ranking  #Retorna o ranking pronto
    except FileNotFoundError:
        #Se o arquivo não for encontrado, retorna uma lista vazia
        return []


#Função para salvar o ranking no arquivo
def salvar_ranking(ranking): #Abre o arquivo no modo escrita e sobrescreve tudo
    # Caminho do arquivo "ranking.txt" relativo a este script
    caminho_ranking = os.path.join(os.path.dirname(__file__), "ranking.txt")

    #Abre o arquivo "ranking.txt" no modo escrita ("w")
    #Esse modo APAGA tudo do conteúdo anterior do arquivo e escreve tudo novamente do zero
    #O WITH garante que o arquivo será fechado automaticamente após terminar o bloco
    #A variável ARQUIVO representa o arquivo aberto para podermos escrever dentro dele
    with open(caminho_ranking, "w") as arquivo:
        for nome, pontos in ranking:
            #Escreve cada jogador no formato: nome;pontos
            arquivo.write(f"{nome};{pontos}\n")


#Função para salvar o histórico de partidas
def salvar_historico(jogador, pontos, numero_secreto):
    # Caminho do arquivo "historico.txt" relativo a este script
    caminho_historico = os.path.join(os.path.dirname(__file__), "historico.txt")

    #Abre o arquivo em modo APPEND, adicionando sempre no final
    #Abre o arquivo "historico.txt" no modo append ("a")
    #Esse modo NÃO apaga o que já existe no arquivo, ele apenas adiciona (anexa) novas linhas ao final
    #O WITH garante que o arquivo será fechado automaticamente ao fim do bloco
    #A variável ARQUIVO representa o arquivo aberto para podermos escrever no histórico
    with open(caminho_historico, "a") as arquivo:
        #Registra cada partida com jogador, pontuação e número secreto
        arquivo.write(f"Jogador: {jogador} | Pontos: {pontos} | Nº secreto: {numero_secreto}\n")


#Função principal do jogo
def jogar():
    while True:  # LOOP INTERNO para permitir jogar novamente ou voltar ao menu
        #Cabeçalho do jogo
        print("=" * 40)
        print(" ***Bem vindo ao Jogo de Adivinhação!*** ")
        print("=" * 40)

        jogador = input("Digite seu nome: ")  #Armazena o nome do jogador

        #Carrega o ranking existente no arquivo
        ranking = carregar_ranking()

        numero_secreto = random.randrange(1, 101)  # era número secreto entre 1 e 100
        total_de_tentativas = 0  #Será definido conforme a dificuldade
        pontos = 1000  #Pontos iniciais do jogador

        #Menu de dificuldade
        print("Qual nível de dificuldade?")
        print("(1) Fácil (2) Médio (3) Difícil")

        #Loop para tratar erro de entrada do nível
        while True:
            try:
                nivel = int(input("Define o nível: "))
                if nivel in [1, 2, 3]:  #Verifica se digitou 1, 2 ou 3
                    break
                else:
                    print("Digite apenas 1, 2 ou 3.")
            except ValueError:
                print("Entrada inválida, digite um número.")

        #Define a quantidade de tentativas conforme o nível
        if nivel == 1:
            total_de_tentativas = 20
        elif nivel == 2:
            total_de_tentativas = 10
        else:
            total_de_tentativas = 5

        #Loop principal para cada tentativa
        for rodada in range(1, total_de_tentativas + 1):
            print(f"Tentativa {rodada} de {total_de_tentativas}")

            #Tratamento de erro do chute
            while True:
                chute_str = input("Digite um número entre 1 e 100: ")
                try:
                    chute = int(chute_str)  #Converte para inteiro
                    if 1 <= chute <= 100:
                        break  #Aceita o chute
                    else:
                        print("Digite um número entre 1 e 100.")
                except ValueError:
                    print("Entrada inválida! Digite apenas números.")

            #Verifica se acertou o número secreto
            if chute == numero_secreto:
                print(f"Parabéns {jogador}! Você acertou e fez {pontos} pontos!")

                #Salva o histórico da partida
                salvar_historico(jogador, pontos, numero_secreto)

                #Adiciona o jogador ao ranking
                ranking.append((jogador, pontos))

                #Ordena do maior para o menor e mantém só os 5 melhores
                ranking = sorted(ranking, key=lambda x: x[1], reverse=True)[:5]

                #Salva ranking atualizado
                salvar_ranking(ranking)

                break  #Encerra o loop de tentativas
            else:
                #Informações sobre o erro do chute
                if chute > numero_secreto:
                    print("Você errou! O seu chute foi MAIOR que o número secreto.")
                else:
                    print("Você errou! O seu chute foi MENOR que o número secreto.")

                #Calcula perdas proporcionalmente a distância do chute
                pontos_perdidos = abs(numero_secreto - chute)
                pontos -= pontos_perdidos  #Atualiza os pontos do jogador

        print("Fim do Jogo!")

        #Exibe o ranking ao final da partida
        print("\n===== TOP 5 JOGADORES =====")
        for pos, (nome, pont) in enumerate(ranking, start=1):
            print(f"{pos}. {nome} - {pont} pontos")
        print("===========================")

        #Pergunta ao usuário se quer jogar novamente
        while True:
            novamente = input("Quer jogar novamente? (s/n): ").lower()

            if novamente == "s":
                break  #Se sim, reinicia o loop while True (jogo novamente)
            elif novamente == "n":
                print("Voltando ao menu principal...")
                return  #Sai da função e volta ao menu principal
            else:
                print("Digite apenas 's' para sim ou 'n' para não.")


#Garante que o jogo só execute se este arquivo for o principal
if __name__ == "__main__":
    jogar()
