class Fila:

    def __init__(self):
        self.itens = []

    def adicionar(self, item):
        self.itens.insert(0, item)
    
    def atender(self):
        if self.is_empty():
            print("A fila está vazia")
            return None
        
        return self.itens.pop()

    def proximo_a_atender(self):
        if self.is_empty():
            print("Não a ninguém para atender")
            return None
        return self.itens[-1]

    def is_empty(self):
        return len(self.itens) == 0
    
    def __str__(self):
        return str(self.itens)