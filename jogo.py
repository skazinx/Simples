import argparse

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
        print(f"\n🎮 Estatísticas do jogo:")
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
        print("✅ Respostas salvas no arquivo 'estatisticas_jogo.txt'.")
    except Exception as e:
        print(f"❌ Erro ao salvar as respostas: {e}")

def main():
    parser = argparse.ArgumentParser(description="Registrar estatísticas de um jogo")

    parser.add_argument('--nome_jogo', type=str, required=True, help='Nome do jogo')
    parser.add_argument('--nome_pessoa', type=str, required=True, help='Nome da pessoa')
    parser.add_argument('--personagem', type=str, required=True, help='Nome do personagem')
    parser.add_argument('--vitorias', type=int, required=True, help='Número de vitórias')
    parser.add_argument('--derrotas', type=int, required=True, help='Número de derrotas')
    parser.add_argument('--eliminacoes', type=int, required=True, help='Número de eliminações')
    parser.add_argument('--mortes', type=int, required=True, help='Número de mortes')

    args = parser.parse_args()

    jogo = Jogo(
        args.nome_jogo,
        args.nome_pessoa,
        args.personagem,
        args.vitorias,
        args.derrotas,
        args.eliminacoes,
        args.mortes
    )

    jogo.mostrar_estatisticas()

    salvar_respostas(jogo)

if __name__ == "__main__":
    main()
