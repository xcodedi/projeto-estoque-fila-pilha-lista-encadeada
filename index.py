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

# Opção 7: Ver fila de vendas pendentes
    elif opcao == "7":
        limpar_tela()
        print("FILA DE VENDAS PENDENTES")
        print("═" * 60)
        vendas.ver_fila_de_vendas()
        pausar()

# Opção 8: Concluir a venda
    elif opcao == "8":
        limpar_tela()
        print("CONCLUIR VENDA")
        print("═" * 40)
        

        venda = vendas.concluir_venda()
        
        if venda:

            sucesso_estoque = estoque.usar_produto(venda['ID_Produto'], venda['Quantidade'])
            
            if sucesso_estoque:

                sistema.adicionar_gasto_ao_cliente(venda['ID_Cliente'], venda['Valor_Total'])
                
                print("\n" + "="*50)
                print("VENDA CONCLUÍDA COM SUCESSO!")
                print("="*50)
                print(f"   ID da Venda: {venda['ID_Venda']}")
                print(f"   Cliente ID: {venda['ID_Cliente']}")
                print(f"   Produto ID: {venda['ID_Produto']}")
                print(f"   Quantidade: {venda['Quantidade']}")
                print(f"   Valor Total: R$ {venda['Valor_Total']:.2f}")
                print(f"   Data: {venda['Data']}")
                print("="*50)
                print("Estoque atualizado!")
                print("Gasto do cliente atualizado!")
            else:
                print("Erro ao atualizar estoque! A venda foi concluída mas o estoque não foi atualizado.")
        else:
            print("Nenhuma venda na fila para concluir!")
        
        pausar()


# Opção 9: Desfazer última operação (cadastro de cliente, cadastro de produto ou registro de venda)
    elif opcao == "9":
        limpar_tela()
        print("DESFAZER ÚLTIMA OPERAÇÃO")
        print("═" * 40)
        
        ultima_operacao = controle_desfazer.desempilhar()
        
        if not ultima_operacao:
            print("Nenhuma operação para desfazer!")
            pausar()
            continue
        
        operacao = ultima_operacao['operacao']
        dados = ultima_operacao['dados']
        
        print(f"\nÚltima operação: {operacao}")
        print(f"   Dados: {dados}")
        print("-" * 40)
        
        desfazer_confirmado = input("Tem certeza que deseja desfazer esta operação? (s/n): ")
        
        if desfazer_confirmado.lower() == 's':

            if operacao == "cadastro_cliente":
                cliente_id = dados['ID']
                cliente_removido = sistema.clientes.remover(cliente_id, chave_id='ID')
                
                if cliente_removido:
                    print(f"Cliente '{dados['Nome']}' removido!")
                    sistema._salvar_arquivo()

            elif operacao == "cadastro_produto":
                produto_id = dados['ID']
                produto_removido = estoque.produtos.remover(produto_id, chave_id='ID')
                
                if produto_removido:
                    print(f"Produto '{dados['Nome']}' removido!")
                    estoque._salvar_na_memoria()

            elif operacao == "registro_venda":
                venda_id = dados['ID_Venda']
                
                vendas_pendentes = []
                fila_temp = vendas.fila_vendas.itens.copy()
                
                while fila_temp:
                    venda_atual = fila_temp.pop()
                    if venda_atual['ID_Venda'] != venda_id:
                        vendas_pendentes.append(venda_atual)
                
                vendas.fila_vendas.itens = []
                for v in reversed(vendas_pendentes):
                    vendas.fila_vendas.adicionar(v)
                
                print(f"Pedido #{venda_id} removido!")
                vendas._salvar_fila()

            else:
                print("Operação não suportada.")

        else:
            print("Cancelado.")
            controle_desfazer.empilhar(operacao, dados)

        pausar()

# Opção 10: Desfazer venda concluída
    elif opcao == "10": 
        limpar_tela()
        print("DESFAZER VENDA CONCLUÍDA")
        print("═" * 50)
        
        vendas_concluidas = vendas.listar_vendas_concluidas()
        
        if not vendas_concluidas:
            pausar()
            continue
        
        try:
            id_venda = int(input("\nDigite o ID da venda que deseja desfazer (ou 0 para cancelar): "))
            
            if id_venda == 0:
                continue
            
            venda_para_desfazer = None
            for venda in vendas_concluidas:
                if venda['ID_Venda'] == id_venda:
                    venda_para_desfazer = venda
                    break
            
            if not venda_para_desfazer:
                print(f"Venda com ID {id_venda} não encontrada!")
                pausar()
                continue
            
            print("\n" + "="*50)
            print("DETALHES DA VENDA:")
            print("="*50)
            print(f"ID Venda: {venda_para_desfazer['ID_Venda']}")
            print(f"ID Cliente: {venda_para_desfazer['ID_Cliente']}")
            print(f"ID Produto: {venda_para_desfazer['ID_Produto']}")
            print(f"Quantidade: {venda_para_desfazer['Quantidade']}")
            print(f"Valor Total: R$ {venda_para_desfazer['Valor_Total']:.2f}")
            print(f"Data: {venda_para_desfazer['Data']}")
            print("="*50)
            
            confirmacao = input("\nTem certeza que deseja desfazer esta venda? (s/n): ")
            
            if confirmacao.lower() == 's':
                sucesso_estoque = estoque.restaurar_estoque(
                    venda_para_desfazer['ID_Produto'], 
                    venda_para_desfazer['Quantidade']
                )
                
                if not sucesso_estoque:
                    print("Erro ao restaurar estoque!")
                    pausar()
                    continue
                
                sucesso_cliente = sistema.subtrair_gasto_do_cliente(
                    venda_para_desfazer['ID_Cliente'],
                    venda_para_desfazer['Valor_Total']
                )
                
                if not sucesso_cliente:
                    print("Erro ao atualizar gasto do cliente!")
                    estoque.usar_produto(
                        venda_para_desfazer['ID_Produto'], 
                        venda_para_desfazer['Quantidade']
                    )
                    pausar()
                    continue
                
                venda_removida = vendas.remover_venda_concluida(id_venda)
                
                if venda_removida:
                    print("\n" + "="*50)
                    print("VENDA DESFEITA COM SUCESSO!")
                    print("="*50)
                    print(f"✓ Estoque restaurado")
                    print(f"✓ Gasto do cliente ajustado")
                    print(f"✓ Venda removida do histórico")
                    print("="*50)
                else:
                    print("Erro ao remover venda do histórico!")
                    estoque.usar_produto(
                        venda_para_desfazer['ID_Produto'], 
                        venda_para_desfazer['Quantidade']
                    )
                    sistema.adicionar_gasto_ao_cliente(
                        venda_para_desfazer['ID_Cliente'],
                        venda_para_desfazer['Valor_Total']
                    )
            else:
                print("Operação cancelada.")
                
        except ValueError:
            print("Digite um número válido!")
        
        pausar()

# Opção 11: Exibir valor total do estoque
    elif opcao == "11":
        limpar_tela()
        print("VALOR TOTAL DO ESTOQUE")
        print("═" * 40)
        estoque.calcular_valor_total_do_estoque()
        pausar()

# Opção 12: Exibir valor total de vendas realizadas
    elif opcao == "12":
        limpar_tela()
        print("VALOR TOTAL DE VENDAS REALIZADAS")
        print("═" * 40)
        vendas.calcular_total_vendas_realizadas()
        pausar()

# Opção 13: Exibir clientes e valores gastos
    elif opcao == "13":
        limpar_tela()
        print("CLIENTES E VALORES GASTOS")
        print("═" * 50)
        sistema.listar_clientes_com_gastos()
        pausar()


    else:
        print("Opção inválida! Tente novamente.")
        pausar()