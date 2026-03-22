class Nodo:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaEncadeada:
    
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0
    
    def inserir_no_fim(self, dado):
        novo_nodo = Nodo(dado)
        
        if self.cabeca is None:
            self.cabeca = novo_nodo
        else:
            atual = self.cabeca
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo_nodo
        
        self.tamanho += 1
        return dado
    
    def inserir_no_inicio(self, dado):
        novo_nodo = Nodo(dado)
        novo_nodo.proximo = self.cabeca
        self.cabeca = novo_nodo
        self.tamanho += 1
        return dado
    
    def remover(self, id_busca, chave_id='ID'):
        if self.cabeca is None:
            return None
        
        if self.cabeca.dado[chave_id] == id_busca:
            removido = self.cabeca.dado
            self.cabeca = self.cabeca.proximo
            self.tamanho -= 1
            return removido
        
        atual = self.cabeca
        while atual.proximo is not None:
            if atual.proximo.dado[chave_id] == id_busca:
                removido = atual.proximo.dado
                atual.proximo = atual.proximo.proximo
                self.tamanho -= 1
                return removido
            atual = atual.proximo
        
        return None
    
    def buscar(self, id_busca, chave_id='ID'):
        atual = self.cabeca
        while atual is not None:
            if atual.dado[chave_id] == id_busca:
                return atual.dado
            atual = atual.proximo
        return None
    
    def listar_todos(self):
        elementos = []
        atual = self.cabeca
        while atual is not None:
            elementos.append(atual.dado)
            atual = atual.proximo
        return elementos
    
    def atualizar(self, id_busca, novos_dados, chave_id='ID'):
        atual = self.cabeca
        while atual is not None:
            if atual.dado[chave_id] == id_busca:
                for chave, valor in novos_dados.items():
                    atual.dado[chave] = valor
                return True
            atual = atual.proximo
        return False
    
    def esta_vazia(self):
        return self.cabeca is None
    
    def __len__(self):
        return self.tamanho
    
    def __str__(self):
        elementos = []
        atual = self.cabeca
        while atual is not None:
            elementos.append(str(atual.dado))
            atual = atual.proximo
        return " -> ".join(elementos) if elementos else "Lista vazia"
