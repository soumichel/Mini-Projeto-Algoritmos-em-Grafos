import networkx as nx

class Grafo:
    @staticmethod
    def construir(dados):
        # Cria um grafo não direcionado usando a biblioteca NetworkX
        grafo = nx.Graph()

        # Itera sobre os dados para construir o grafo
        for entry in dados:
            userId = entry.get('review/userId')
            productId = entry.get('product/productId')
            pontuacao = float(entry.get('review/score', 0))

            # Verifica se os IDs do usuário e do produto estão presentes nos dados
            if userId and productId:
                # Adiciona nós para o usuário e o produto, e uma aresta conectando-os com uma pontuação
                grafo.add_node(userId)
                grafo.add_node(productId)
                grafo.add_edge(userId, productId, pontuacao=pontuacao)

        return grafo
