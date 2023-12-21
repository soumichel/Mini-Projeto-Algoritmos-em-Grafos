# .PHONY indica que 'all', 'install', 'run' e 'clean' não são arquivos reais
.PHONY: all install run clean

# Regra padrão: 'make' sozinho executa 'install', 'run' e 'clean'
all: install run clean

# Instala dependências usando pip3
install:
	pip3 install networkx

# Executa o script principal
run:
	python3 src/main.py

# Limpa arquivos temporários e caches
clean:
	rm -rf src/__pycache__
	rm -f *.pyc
