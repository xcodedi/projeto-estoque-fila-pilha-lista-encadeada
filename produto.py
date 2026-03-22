import os
from lista_encadeada import ListaEncadeada

class Produto:
    
    def __init__(self):
        self.produtos = ListaEncadeada()
        self.proximo_id_captura = 1
        self.arquivo_produto = "produtos.txt"
        
        self._carregar_da_memoria()
    
    def _carregar_da_memoria(self):
        if not os.path.exists(self.arquivo_produto):
            self._criar_arquivo_padrao()
            return
        
        try:
            with open(self.arquivo_produto, "r", encoding="utf-8") as arquivo_lertxt:
                linhas = arquivo_lertxt.readlines()
                
                inicio = 1 if len(linhas) > 0 and "ID" in linhas[0] else 0
                
                for linha in linhas[inicio:]:
                    linha = linha.strip()
                    if not linha:
                        continue
                    
                    try:
                        id_str = linha[0:5].strip()
                        nome_str = linha[5:25].strip()
                        qtd_str = linha[25:40].strip()
                        preco_str = linha[40:].strip()
                        
                        id_produto = int(id_str)
                        
                        produto = {
                            "ID": id_produto,
                            "Nome": nome_str,
                            "Quantidade": int(qtd_str),
                            "Preco": float(preco_str)
                        }
                        
                        self.produtos.inserir_no_fim(produto)
                        
                        if id_produto >= self.proximo_id_captura:
                            self.proximo_id_captura = id_produto + 1
                            
                    except ValueError as erro_leitura:
                        print(f"Erro ao ler linha: {linha} - {erro_leitura}")
                        continue
                        
        except Exception as erro_carregar:
            print(f"Erro ao carregar produtos: {erro_carregar}")
            self._criar_arquivo_padrao()
    
    def _criar_arquivo_padrao(self):
        try:
            with open(self.arquivo_produto, "w", encoding="utf-8") as arquivo_criacao:
                arquivo_criacao.write(f"{'ID':<5}{'Nome':<20}{'Quantidade':<15}{'Preco':<10}\n")
                arquivo_criacao.write("-" * 55 + "\n")
        except Exception as erro_criar:
            print(f"Erro ao criar arquivo de produtos: {erro_criar}")
    
    def _salvar_na_memoria(self):
        try:
            with open(self.arquivo_produto, "w", encoding="utf-8") as arquivo_escrevetxt:
                arquivo_escrevetxt.write(f"{'ID':<5}{'Nome':<20}{'Quantidade':<15}{'Preco':<10}\n")
                arquivo_escrevetxt.write("-" * 55 + "\n")
                
                todos_produtos = self.produtos.listar_todos()
                for produto in todos_produtos:
                    arquivo_escrevetxt.write(
                        f"{produto['ID']:<5}{produto['Nome']:<20}"
                        f"{produto['Quantidade']:<15}{produto['Preco']:<10.2f}\n"
                    )
        except Exception as erro_salvar:
            print(f"Erro ao salvar produtos: {erro_salvar}")
    
    def capturar_produto(self, nome_produto, quantidade_produto, preco_produto):
        if not nome_produto or nome_produto.strip() == "":
            print("Erro: Nome do produto não pode ser vazio!")
            return None
        
        if quantidade_produto < 0:
            print("Erro: Quantidade não pode ser negativa!")
            return None
        
        if preco_produto <= 0:
            print("Erro: Preço deve ser maior que zero!")
            return None
        
        novo_produto = {
            "ID": self.proximo_id_captura,
            "Nome": nome_produto.strip(),
            "Quantidade": quantidade_produto,
            "Preco": float(preco_produto)
        }
        
        self.produtos.inserir_no_fim(novo_produto)
        self.proximo_id_captura += 1
        
        self._salvar_na_memoria()
        
        print(f"Produto {nome_produto} cadastrado com sucesso (ID: {novo_produto['ID']})!")
        return novo_produto