from FORCA import forca
from ADIVINHACAO import Adivinhacao


def escolhe_jogo():
    while True:
        print("=" * 40)
        print("*********Escolha o Jogo!*********")
        print("=" * 40)
        print("(1) Forca (2) Adivinhação (0) Sair")

        # Loop para validar a entrada do usuário
        try:
            jogo = int(input("Escolha o jogo: "))
            if jogo in [0, 1, 2]:
                pass
            else:
                print("Escolha inválida. Digite 1, 2 ou 0 para sair.")
                continue
        except ValueError:
            print("Entrada inválida. Digite um número.")
            continue

        # Executa o jogo escolhido ou sai do programa
        if jogo == 1:
            print("Jogando FORCA")
            forca.jogar()
        elif jogo == 2:
            print("Jogando ADIVINHACAO")
            Adivinhacao.jogar()
        elif jogo == 0:
            print("Saindo do programa. Até logo!")
            break

if __name__ == "__main__":
    escolhe_jogo()
