class NodoPilha:
    def __init__(self, operacao, dados):
        self.operacao = operacao
        self.dados = dados
        self.anterior = None

class Pilha:
    def __init__(self):
        self.topo = None
        self._tamanho = 0

    def empilhar(self, operacao, dados):
        novo_nodo = NodoPilha(operacao, dados)

        if self.topo is not None:
            novo_nodo.anterior = self.topo

        self.topo = novo_nodo
        self._tamanho += 1

    def desempilhar(self):
        if self.esta_vazia():
            return None

        removido = self.topo
        self.topo = self.topo.anterior
        self._tamanho -= 1

        return {
            "operacao": removido.operacao,
            "dados": removido.dados
        }

    def ver_topo(self):
        if self.esta_vazia():
            return None

        return {
            "operacao": self.topo.operacao,
            "dados": self.topo.dados
        }

    def esta_vazia(self):
        return self.topo is None

    def tamanho(self):
        return self._tamanho

    def limpar(self):
        self.topo = None
        self._tamanho = 0

    def __len__(self):
        return self._tamanho

    def __str__(self):
        elementos = []
        atual = self.topo

        while atual is not None:
            elementos.append(f"{atual.operacao}")
            atual = atual.anterior

        return "Topo -> " + " -> ".join(elementos) if elementos else "Pilha vazia"