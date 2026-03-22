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
