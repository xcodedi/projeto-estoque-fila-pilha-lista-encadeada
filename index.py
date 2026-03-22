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

# Opção 0: Sair do sistema
    if opcao == "0":
        print("\nEncerrando o sistema")
        break

# Opção 1: Realizar o cadastro de cliente
    elif opcao == "1":
        limpar_tela()
        print("CADASTRAR NOVO CLIENTE")
        print("═" * 40)
        
        nome = input("Digite o nome do cliente (ou 0 para voltar): ")
        
        if nome == "0":
            continue
        
        resultado = sistema.cadastrar_cliente(nome)
        
        if resultado:

            controle_desfazer.empilhar("cadastro_cliente", resultado)
            print(f"Cliente {nome} cadastrado com sucesso! (ID: {resultado['ID']})")
        else:
            print("Falha ao cadastrar cliente. Verifique as regras")
        
        pausar()

# Opção 2: Exibir lista de clientes cadastrados
    elif opcao == "2":
        limpar_tela()
        print("LISTA DE CLIENTES CADASTRADOS")
        print("═" * 50)
        sistema.listar_clientes()
        pausar()

# Opção 3: Realizar o cadastro de produtos
    elif opcao == "3":
        limpar_tela()
        print("CADASTRAR NOVO PRODUTO")
        print("═" * 40)
        
        nome = input("Digite o nome do produto (ou 0 para voltar): ")
        
        if nome == "0":
            continue
        

        if not nome.replace(" ", "").isalpha():
            print("Nome inválido! Use apenas letras.")
            pausar()
            continue

        try:
            quantidade = int(input("Digite a quantidade em estoque: "))
            if quantidade < 0:
                print("Quantidade não pode ser negativa!")
                pausar()
                continue
        except ValueError:
            print("Digite um número inteiro válido!")
            pausar()
            continue

        try:
            preco = float(input("Digite o preço unitário: R$ "))
            if preco <= 0:
                print("Preço deve ser maior que zero!")
                pausar()
                continue
        except ValueError:
            print("Digite um valor numérico válido!")
            pausar()
            continue

        resultado = estoque.capturar_produto(nome, quantidade, preco)
        
        if resultado:

            controle_desfazer.empilhar("cadastro_produto", resultado)
        else:
            print("Falha ao cadastrar produto.")
        
        pausar()

# Opção 4: Exibir lista de produtos cadastrados
    elif opcao == "4":
        limpar_tela()
        print("LISTA DE PRODUTOS EM ESTOQUE")
        print("═" * 60)
        estoque.listar_produtos_cadastrados()
        pausar()

# Opção 5: Pesquisar produto por ID ou nome
    elif opcao == "5":
        limpar_tela()
        print("PESQUISAR PRODUTO")
        print("═" * 40)
        
        print("1 - Pesquisar por ID")
        print("2 - Pesquisar por nome")
        sub_opcao = input("Escolha: ")
        
        if sub_opcao == "1":
            id_produto = input("Digite o ID do produto: ")
            produto = estoque.buscar_produto_por_id(id_produto)
            
            if produto:
                print("\nPRODUTO ENCONTRADO:")
                print(f"   ID: {produto['ID']}")
                print(f"   Nome: {produto['Nome']}")
                print(f"   Quantidade: {produto['Quantidade']}")
                print(f"   Preço: R$ {produto['Preco']:.2f}")
            else:
                print(f"Produto com ID {id_produto} não encontrado!")
                
        elif sub_opcao == "2":
            nome = input("Digite o nome (ou parte do nome): ")
            resultados = estoque.buscar_por_nome(nome)
            
            if resultados:
                print(f"\n{len(resultados)} produto(s) encontrado(s):")
                for p in resultados:
                    print(f"   ID: {p['ID']} | {p['Nome']} | Qtd: {p['Quantidade']} | R$ {p['Preco']:.2f}")
            else:
                print(f"Nenhum produto encontrado com '{nome}'")
        else:
            print("Opção inválida!")
        
        pausar()

# Opção 6: Registrar venda (adicionar à fila de vendas)
    elif opcao == "6":
        limpar_tela()
        print("REGISTRAR PEDIDO (FILA DE VENDAS)")
        print("═" * 40)
        

        id_cliente = input("Digite o ID do cliente: ")
        cliente = sistema.buscar_cliente_por_id(id_cliente)
        
        if not cliente:
            print("Cliente não encontrado!")
            pausar()
            continue
        

        print("\nProdutos disponíveis:")
        todos_produtos = estoque.produtos.listar_todos()
        if not todos_produtos:
            print("   Nenhum produto cadastrado!")
            pausar()
            continue
            
        for p in todos_produtos:
            print(f"   ID: {p['ID']} | {p['Nome']} | Qtd: {p['Quantidade']} | R$ {p['Preco']:.2f}")
        

        id_produto = input("\nDigite o ID do produto: ")
        produto = estoque.buscar_produto_por_id(id_produto)
        
        if not produto:
            print("Produto não encontrado!")
            pausar()
            continue

        try:
            quantidade = int(input(f"Digite a quantidade (máx: {produto['Quantidade']}): "))
            
            if quantidade <= 0:
                print("Quantidade deve ser maior que zero!")
            elif quantidade > produto['Quantidade']:
                print("Estoque insuficiente!")
            else:
                valor_total = quantidade * produto['Preco']
                

                venda = vendas.registrar_venda(
                    cliente['ID'], 
                    produto['ID'], 
                    quantidade, 
                    valor_total
                )
                
                if venda:

                    controle_desfazer.empilhar("registro_venda", venda)
                    print(f"Pedido registrado na fila! Total: R$ {valor_total:.2f}")
                else:
                    print("Falha ao registrar venda!")
                
        except ValueError:
            print("Digite um número inteiro válido!")
        
        pausar()