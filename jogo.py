class Jogo:
    def __init__(self, nome_jogo, nome_pessoa, personagem, vitorias, derrotas, eliminacoes, mortes):
        self.nome_jogo = nome_jogo
        self.nome_pessoa = nome_pessoa
        self.personagem = personagem
        self.vitorias = vitorias
        self.derrotas = derrotas
        self.eliminacoes = eliminacoes
        self.mortes = mortes

    def mostrar_estatisticas(self):
        print(f"Jogo: {self.nome_jogo}")
        print(f"Nome da pessoa: {self.nome_pessoa}")
        print(f"Personagem: {self.personagem}")
        print(f"Vitórias: {self.vitorias}")
        print(f"Derrotas: {self.derrotas}")
        print(f"Eliminações: {self.eliminacoes}")
        print(f"Mortes: {self.mortes}")

def salvar_respostas(jogo):
    try:
        with open("estatisticas_jogo.txt", "w") as arquivo:
            arquivo.write(f"Jogo: {jogo.nome_jogo}\n")
            arquivo.write(f"Nome da pessoa: {jogo.nome_pessoa}\n")
            arquivo.write(f"Personagem: {jogo.personagem}\n")
            arquivo.write(f"Vitórias: {jogo.vitorias}\n")
            arquivo.write(f"Derrotas: {jogo.derrotas}\n")
            arquivo.write(f"Eliminações: {jogo.eliminacoes}\n")
            arquivo.write(f"Mortes: {jogo.mortes}\n")
        print("Respostas salvas com sucesso no arquivo 'estatisticas_jogo.txt'.")
    except Exception as e:
        print(f"Erro ao salvar as respostas: {e}")

def main():
    while True:
        nome_jogo = input("Digite o nome do jogo: ")
        nome_pessoa = input("Digite o nome da pessoa: ")
        personagem = input("Digite o nome do personagem: ")
        vitorias = int(input("Digite a quantidade de vitórias: "))
        derrotas = int(input("Digite a quantidade de derrotas: "))
        eliminacoes = int(input("Digite a quantidade de eliminações: "))
        mortes = int(input("Digite a quantidade de mortes: "))

        jogo = Jogo(nome_jogo, nome_pessoa, personagem, vitorias, derrotas, eliminacoes, mortes)

        while True:
            print("\nMenu:")
            print("1. Mostrar estatísticas do jogo")
            print("2. Salvar respostas")
            print("3. Fazer as mesmas perguntas novamente")
            print("4. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                jogo.mostrar_estatisticas()
            elif opcao == "2":
                salvar_respostas(jogo)
            elif opcao == "3":
                break
            elif opcao == "4":
                print("Programa encerrado.")
                return
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
