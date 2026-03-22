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

    def buscar_produto_por_id(self, id_produto):
        try:
            id_busca = int(id_produto) if isinstance(id_produto, str) else id_produto
            return self.produtos.buscar(id_busca, chave_id='ID')
        except (ValueError, TypeError):
            return None
    
    def buscar_por_nome(self, nome_produto):
        if not nome_produto:
            return []
        
        nome_busca = nome_produto.lower().strip()
        resultados = []
        todos = self.produtos.listar_todos()
        
        for produto in todos:
            if nome_busca in produto['Nome'].lower():
                resultados.append(produto)
        
        return resultados
    
    def usar_produto(self, id_produto, quantidade_usada):
        produto = self.buscar_produto_por_id(id_produto)
        
        if produto is None:
            print(f"Erro: Produto ID {id_produto} não encontrado!")
            return False
        
        if quantidade_usada <= 0:
            print("Erro: Quantidade deve ser maior que zero!")
            return False
        
        if produto['Quantidade'] < quantidade_usada:
            print(f"Erro: Estoque insuficiente! Disponível: {produto['Quantidade']}, Solicitado: {quantidade_usada}")
            return False
        
        nova_quantidade = produto['Quantidade'] - quantidade_usada
        sucesso = self.produtos.atualizar(id_produto, {'Quantidade': nova_quantidade}, chave_id='ID')
        
        if sucesso:
            self._salvar_na_memoria()
            print(f"Estoque atualizado: {produto['Nome']} agora tem {nova_quantidade} unidades")
            return True
        else:
            print("Erro ao atualizar estoque")
            return False
    
    def repor_estoque(self, id_produto, quantidade_reposicao):
        produto = self.buscar_produto_por_id(id_produto)
        
        if produto is None:
            print(f"Erro: Produto ID {id_produto} não encontrado!")
            return False
        
        if quantidade_reposicao <= 0:
            print("Erro: Quantidade de reposição deve ser maior que zero!")
            return False
        
        nova_quantidade = produto['Quantidade'] + quantidade_reposicao
        sucesso = self.produtos.atualizar(id_produto, {'Quantidade': nova_quantidade}, chave_id='ID')
        
        if sucesso:
            self._salvar_na_memoria()
            print(f"Estoque reposto: {produto['Nome']} agora tem {nova_quantidade} unidades")
            return True
        return False
    
    def listar_produtos_cadastrados(self):
        todos = self.produtos.listar_todos()
        
        if not todos:
            print("Nenhum produto cadastrado")
            return []
        
        print("\n" + "="*60)
        print("PRODUTOS CADASTRADOS")
        print("="*60)
        print(f"{'ID':<5} {'NOME':<20} {'QUANTIDADE':<15} {'PREÇO':<10}")
        print("-"*60)
        
        for p in todos:
            print(f"{p['ID']:<5} {p['Nome']:<20} {p['Quantidade']:<15} R$ {p['Preco']:<10.2f}")
        
        print("="*60)
        return todos
    
    def calcular_valor_total_do_estoque(self):
        todos = self.produtos.listar_todos()
        valor_total = sum(p['Quantidade'] * p['Preco'] for p in todos)
        
        print(f"\nValor total do estoque: R$ {valor_total:.2f}")
        return valor_total
    
    def restaurar_estoque(self, id_produto, quantidade):
        produto = self.buscar_produto_por_id(id_produto)
        
        if produto is None:
            print(f"Erro: Produto ID {id_produto} não encontrado!")
            return False
        
        if quantidade <= 0:
            print("Erro: Quantidade deve ser maior que zero!")
            return False
        
        nova_quantidade = produto['Quantidade'] + quantidade
        sucesso = self.produtos.atualizar(id_produto, {'Quantidade': nova_quantidade}, chave_id='ID')
        
        if sucesso:
            self._salvar_na_memoria()
            print(f"Estoque restaurado: {produto['Nome']} agora tem {nova_quantidade} unidades")
            return True
        return False
