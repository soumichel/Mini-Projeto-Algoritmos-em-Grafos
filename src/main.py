import os
import random
from dados import Dados
from grafo import Grafo
from recomendador import Recomendador

# Obtém o diretório atual do script
current_directory = os.path.dirname(os.path.abspath(__file__))

class Main:
    @staticmethod
    def exibirDadosGrafo(grafo):
        # Obtém e imprime o número de nós e arestas no grafo
        numNodes = grafo.number_of_nodes()
        numEdges = grafo.number_of_edges()

        print(f'Quantidade de nós: {numNodes}')
        print(f'Quantidade de arestas: {numEdges}')

    @staticmethod
    def exibirDadosUsuarioAleatorio(grafo):
        # Obtém um usuário aleatório do grafo e exibe seu ID
        usuarios = [node for node in grafo.nodes if not node.startswith("product/")]

        if usuarios:
            userId = random.choice(usuarios)
            print(f"ID do usuário aleatório: {userId}")
        else:
            print('Não há usuários disponíveis para análise.')

    @staticmethod
    def recomendarFilmesParaUsuario(grafo, userId):
        # Verifica se o usuário existe no grafo e recomenda filmes para ele
        if userId in grafo.nodes:
            filmesRecomendadosIds = Recomendador.recomendar(grafo, userId)

            if filmesRecomendadosIds:
                print(f'Filmes recomendados para o usuário {userId}:')
                for filmeId in filmesRecomendadosIds:
                    print(f'- {filmeId}')
            else:
                print(f'Não há filmes recomendados para o usuário {userId}.')
        else:
            print(f'O ID do usuário {userId} não foi encontrado.')

    @staticmethod
    def exibirMenu():
        # Exibe as opções disponíveis no menu
        print("1. Visualizar dados do grafo")
        print("2. Visualizar dados de um usuário aleatório na base de dados")
        print("3. Recomendar filmes para um usuário aleatório")
        print("0. Sair")

    @staticmethod
    def executar():
        # Configuração inicial: leitura de dados, construção do grafo
        filePath = 'amostra-grafo-movies.txt'
        limiteDeDados = 5000 # Limite pode ser alterado conforme a base de dados
        dados = Dados.ler(filePath, limite=limiteDeDados)
        grafo = Grafo.construir(dados)

        while True:
            Main.exibirMenu()
            opcao = input("Escolha uma opção (0-3): ")

            if opcao == '0':
                print("Encerrando o programa.")
                break
            elif opcao == '1':
                Main.exibirDadosGrafo(grafo)
            elif opcao == '2':
                Main.exibirDadosUsuarioAleatorio(grafo)
            elif opcao == '3':
                # Obtém um usuário aleatório e recomenda filmes para ele
                usuarios = [node for node in grafo.nodes if not node.startswith("product/")]
                if usuarios:
                    userId = random.choice(usuarios)
                    Main.recomendarFilmesParaUsuario(grafo, userId)
                else:
                    print('Não há usuários disponíveis para análise.')
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    Main.executar()


# J. McAuley and J. Leskovec. From amateurs to connoisseurs: modeling the evolution of user expertise through online reviews. WWW, 2013.