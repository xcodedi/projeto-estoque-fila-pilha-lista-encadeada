import os
from cliente import Cliente
from produto import Produto
from venda import Vendas
from pilha import Pilha

sistema = Cliente()
estoque = Produto()
controle_desfazer = Pilha()
vendas = Vendas()

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

#professor este trecho foi solicitado para IA desenhar a tabela
def exibir_menu():
    print(""" 
    ╔════════════════════════════════════════╗
    ║        MENU ESTOQUE E VENDAS           ║
    ╠════════════════════════════════════════╣
    ║ 1 - Cadastrar cliente                  ║
    ║ 2 - Listar clientes                    ║
    ║ 3 - Cadastrar produto                  ║
    ║ 4 - Listar produtos                    ║
    ║ 5 - Pesquisar produto                  ║
    ║ 6 - Registrar pedido (fila)            ║
    ║ 7 - Ver fila de vendas                 ║
    ║ 8 - Concluir venda                     ║
    ║ 9 - Desfazer última operação para      ║
    ║  (cadastro-clientes,cadastro-produto   ║
    ║    e fila de vendas)                   ║
    ║                                        ║
    ║ 10 - Desfazer venda concluída          ║
    ║ 11 - Exibir valor total do estoque     ║
    ║ 12 - Exibir valor total de vendas      ║
    ║ 13 - Exibir clientes e valores gastos  ║
    ║ 0 - Sair                               ║
    ╚════════════════════════════════════════╝
    """)

def pausar():
    input("\nPressione Enter para continuar")

while True:
    limpar_tela()
    exibir_menu()
    opcao = input("Digite a opção desejada: ")