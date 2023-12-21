class Dados:
    @staticmethod
    def ler(filePath, limite=None):
        # Inicializa uma lista para armazenar os dados lidos do arquivo
        dados = []

        # Abre o arquivo para leitura usando a codificação 'latin-1'
        with open(filePath, 'r', encoding='latin-1') as file:
            # Inicializa um dicionário para armazenar as entradas (chave-valor) dos dados
            entry = {}
            for line in file:
                # Processa linhas que começam com "product/" ou "review/"
                if line.startswith("product/") or line.startswith("review/"):
                    # Divide a linha no primeiro ": " para obter a chave e o valor
                    key, value = line.strip().split(': ', 1)
                    entry[key] = value
                # Processa linhas em branco, indicando uma nova entrada de dados
                elif not line.strip() and entry:
                    # Adiciona a entrada ao conjunto de dados e reinicializa o dicionário
                    dados.append(entry)
                    entry = {}
                    # Verifica se atingiu o limite especificado
                    if limite is not None and len(dados) >= limite:
                        break

        return dados
