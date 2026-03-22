import os
from fila import Fila
from datetime import datetime

class Vendas:
    
    def __init__(self):
        self.fila_vendas = Fila()
        self.historico_vendas = []
        self.proximo_id_venda = 1
        self.arquivo_vendas = "vendas.txt"
        self.arquivo_historico = "historico_vendas.txt"
        
        self._carregar_vendas()
    
    def _carregar_vendas(self):
        if os.path.exists(self.arquivo_historico):
            try:
                with open(self.arquivo_historico, "r", encoding="utf-8") as f:
                    linhas = f.readlines()
                    inicio = 1 if len(linhas) > 0 and "ID" in linhas[0] else 0
                    
                    for linha in linhas[inicio:]:
                        linha = linha.strip()
                        if not linha:
                            continue
                        
                        try:
                            partes = linha.split('|')
                            if len(partes) >= 6:
                                venda = {
                                    "ID_Venda": int(partes[0].strip()),
                                    "ID_Cliente": int(partes[1].strip()),
                                    "ID_Produto": int(partes[2].strip()),
                                    "Quantidade": int(partes[3].strip()),
                                    "Valor_Total": float(partes[4].strip()),
                                    "Data": partes[5].strip()
                                }
                                self.historico_vendas.append(venda)
                                
                                if venda["ID_Venda"] >= self.proximo_id_venda:
                                    self.proximo_id_venda = venda["ID_Venda"] + 1
                        except (ValueError, IndexError):
                            continue
            except Exception as e:
                print(f"Erro ao carregar histórico: {e}")
        
        if os.path.exists(self.arquivo_vendas):
            try:
                with open(self.arquivo_vendas, "r", encoding="utf-8") as f:
                    linhas = f.readlines()
                    inicio = 1 if len(linhas) > 0 and "ID" in linhas[0] else 0
                    
                    for linha in linhas[inicio:]:
                        linha = linha.strip()
                        if not linha:
                            continue
                        
                        try:
                            partes = linha.split('|')
                            if len(partes) >= 5:
                                venda = {
                                    "ID_Venda": int(partes[0].strip()),
                                    "ID_Cliente": int(partes[1].strip()),
                                    "ID_Produto": int(partes[2].strip()),
                                    "Quantidade": int(partes[3].strip()),
                                    "Valor_Total": float(partes[4].strip()),
                                    "Data": partes[5].strip() if len(partes) > 5 else "Pendente"
                                }
                                self.fila_vendas.adicionar(venda)

                                if venda["ID_Venda"] >= self.proximo_id_venda:
                                    self.proximo_id_venda = venda["ID_Venda"] + 1

                        except (ValueError, IndexError):
                            continue
            except Exception as e:
                print(f"Erro ao carregar fila de vendas: {e}")

        self._garantir_arquivos()
    
    def _garantir_arquivos(self):
        for arquivo in [self.arquivo_vendas, self.arquivo_historico]:
            if not os.path.exists(arquivo):
                try:
                    with open(arquivo, "w", encoding="utf-8") as f:
                        f.write(f"{'ID':<10}|{'Cliente':<10}|{'Produto':<10}|{'Qtd':<5}|{'Total':<10}|{'Data':<20}\n")
                        f.write("-" * 70 + "\n")
                except Exception as e:
                    print(f"Erro ao criar arquivo {arquivo}: {e}")
    
    def _salvar_fila(self):
        try:
            with open(self.arquivo_vendas, "w", encoding="utf-8") as f:
                f.write(f"{'ID':<10}|{'Cliente':<10}|{'Produto':<10}|{'Qtd':<5}|{'Total':<10}|{'Data':<20}\n")
                f.write("-" * 70 + "\n")
                
                vendas_pendentes = list(reversed(self.fila_vendas.itens))
                for venda in vendas_pendentes:
                    f.write(
                        f"{venda['ID_Venda']:<10}|{venda['ID_Cliente']:<10}|"
                        f"{venda['ID_Produto']:<10}|{venda['Quantidade']:<5}|"
                        f"{venda['Valor_Total']:<10.2f}|{venda.get('Data', 'Pendente'):<20}\n"
                    )
        except Exception as e:
            print(f"Erro ao salvar fila de vendas: {e}")
    
    def _salvar_historico(self):
        try:
            with open(self.arquivo_historico, "w", encoding="utf-8") as f:
                f.write(f"{'ID':<10}|{'Cliente':<10}|{'Produto':<10}|{'Qtd':<5}|{'Total':<10}|{'Data':<20}\n")
                f.write("-" * 70 + "\n")
                
                for venda in self.historico_vendas:
                    f.write(
                        f"{venda['ID_Venda']:<10}|{venda['ID_Cliente']:<10}|"
                        f"{venda['ID_Produto']:<10}|{venda['Quantidade']:<5}|"
                        f"{venda['Valor_Total']:<10.2f}|{venda.get('Data', 'N/A'):<20}\n"
                    )
        except Exception as e:
            print(f"Erro ao salvar histórico: {e}")
    
