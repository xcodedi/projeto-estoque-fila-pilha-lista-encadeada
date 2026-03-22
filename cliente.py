import os
from lista_encadeada import ListaEncadeada

class Cliente:
    
    def __init__(self):
        self.clientes = ListaEncadeada()
        self.proximo_id_cliente = 1
        self.arquivo = "clientes.txt"
        
        self._carregar_arquivo()
    
    def _carregar_arquivo(self):
        if not os.path.exists(self.arquivo):
            self._criar_arquivo_padrao()
            return
            
        try:
            with open(self.arquivo, "r", encoding="utf-8") as arquivo_lertxt:
                linhas = arquivo_lertxt.readlines()
                
                inicio = 1 if len(linhas) > 0 and "ID" in linhas[0] else 0
                
                for linha in linhas[inicio:]:
                    linha = linha.strip()
                    if not linha:
                        continue
                    
                    try:
                        id_str = linha[0:5].strip()
                        nome_str = linha[5:25].strip()
                        gasto_str = linha[25:].strip()
                        
                        id_cliente = int(id_str)
                        
                        cliente = {
                            "ID": id_cliente,
                            "Nome": nome_str,
                            "Gasto Total": float(gasto_str) if gasto_str else 0.0
                        }
                        
                        self.clientes.inserir_no_fim(cliente)
                        
                        if id_cliente >= self.proximo_id_cliente:
                            self.proximo_id_cliente = id_cliente + 1
                            
                    except ValueError as erro_ler_cliente:
                        print(f"Erro ao ler cliente: {linha} - {erro_ler_cliente}")
                        continue
                        
        except Exception as erro_carregamento:
            print(f"Erro ao carregar clientes: {erro_carregamento}")
            self._criar_arquivo_padrao()
    
    def _criar_arquivo_padrao(self):
        try:
            with open(self.arquivo, "w", encoding="utf-8") as f:
                f.write(f"{'ID':<5}{'Nome':<20}{'Gasto Total':<15}\n")
                f.write("-" * 45 + "\n")
        except Exception as e:
            print(f"Erro ao criar arquivo de clientes: {e}")
    
    def _salvar_arquivo(self):
        try:
            with open(self.arquivo, "w", encoding="utf-8") as arquivo_salvar_cliente:
                arquivo_salvar_cliente.write(f"{'ID':<5}{'Nome':<20}{'Gasto Total':<15}\n")
                arquivo_salvar_cliente.write("-" * 45 + "\n")
                
                todos_clientes = self.clientes.listar_todos()
                for c in todos_clientes:
                    arquivo_salvar_cliente.write(f"{c['ID']:<5}{c['Nome']:<20}{c['Gasto Total']:<15.2f}\n")
        except Exception as e:
            print(f"Erro ao salvar clientes: {e}")
    
    def cadastrar_cliente(self, nome_cliente):


        if not nome_cliente or nome_cliente.strip() == "":
            print("Erro: Nome do cliente não pode ser vazio!")
            return None
        

        if not all(palavra.isalpha() for palavra in nome_cliente.split()):
            print("Erro: Nome deve conter apenas letras!")
            return None
        
        novo_cliente = {
            "ID": self.proximo_id_cliente,
            "Nome": nome_cliente.strip(),
            "Gasto Total": 0.0
        }
        
        self.clientes.inserir_no_fim(novo_cliente)
        self.proximo_id_cliente += 1
        
        self._salvar_arquivo()
        return novo_cliente
   
    def buscar_cliente_por_id(self, id_cliente):
        try:
            id_busca = int(id_cliente) if isinstance(id_cliente, str) else id_cliente
            return self.clientes.buscar(id_busca, chave_id='ID')
        except (ValueError, TypeError):
            return None
    
    def adicionar_gasto_ao_cliente(self, id_cliente, valor):
        cliente = self.buscar_cliente_por_id(id_cliente)
        
        if cliente is None:
            print(f"Erro: Cliente ID {id_cliente} não encontrado!")
            return False
        
        if valor <= 0:
            print("Erro: Valor do gasto deve ser positivo!")
            return False
        
        novo_gasto = cliente["Gasto Total"] + valor
        sucesso = self.clientes.atualizar(id_cliente, {'Gasto Total': novo_gasto}, chave_id='ID')
        
        if sucesso:
            self._salvar_arquivo()
            print(f" Gasto de R$ {valor:.2f} adicionado a {cliente['Nome']}")
            return True
        return False
    
    def listar_clientes(self):
        todos = self.clientes.listar_todos()
        
        if not todos:
            print(" Nenhum cliente cadastrado")
            return []
        
        print("\n" + "="*50)
        print("CLIENTES CADASTRADOS")
        print("="*50)
        print(f"{'ID':<5} {'NOME':<20} {'GASTO TOTAL':<15}")
        print("-"*50)
        
        for c in todos:
            print(f"{c['ID']:<5} {c['Nome']:<20} R$ {c['Gasto Total']:<15.2f}")
        
        print("="*50)
        return todos
    
    def listar_clientes_com_gastos(self):
        return self.listar_clientes()
    
    def subtrair_gasto_do_cliente(self, id_cliente, valor):
        cliente = self.buscar_cliente_por_id(id_cliente)
        
        if cliente is None:
            print(f"Erro: Cliente ID {id_cliente} não encontrado!")
            return False
        
        if valor <= 0:
            print("Erro: Valor deve ser positivo!")
            return False
        
        novo_gasto = max(0, cliente["Gasto Total"] - valor)
        sucesso = self.clientes.atualizar(id_cliente, {'Gasto Total': novo_gasto}, chave_id='ID')
        
        if sucesso:
            self._salvar_arquivo()
            print(f"R$ {valor:.2f} subtraído do gasto de {cliente['Nome']}")
            print(f"Novo gasto total: R$ {novo_gasto:.2f}")
            return True
        return False