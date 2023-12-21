import random

class Recomendador:
    @staticmethod
    def recomendar(grafo, userId, numFilmes=5):
        filmesAvaliados = {filme: grafo[userId][filme]['pontuacao'] for filme in grafo.neighbors(userId)}
        filmesNaoAvaliados = {filme: 0 for filme in grafo.nodes if not grafo.has_edge(userId, filme)}

        # Utiliza o algoritmo de filtragem colaborativa para recomendar filmes
        filmesRecomendadosIds = Recomendador.filtragemColaborativa(grafo, userId, filmesNaoAvaliados, numFilmes)

        return filmesRecomendadosIds

    @staticmethod
    def filtragemColaborativa(grafo, userId, filmesNaoAvaliados, numFilmes):
        # Algoritmo de filtragem colaborativa ponderada: recomendar filmes com base nas pontuações dos usuários similares
        pontuacoesSimilares = {}
        for vizinho in grafo.neighbors(userId):
            for filme in filmesNaoAvaliados:
                if grafo.has_edge(vizinho, filme):
                    pontuacaoVizinho = grafo[userId][vizinho]['pontuacao']
                    pontuacoesSimilares[filme] = pontuacoesSimilares.get(filme, 0) + pontuacaoVizinho

        # Ordenar os filmes recomendados com base nas pontuações similares
        filmesRecomendadosIds = sorted(pontuacoesSimilares, key=pontuacoesSimilares.get, reverse=True)[:numFilmes]

        return filmesRecomendadosIds
