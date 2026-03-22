# 📦 Sistema de Estoque e Vendas em Python

## 📚 Disciplina

**ORGANIZAÇÃO E ABSTRAÇÃO NA PROGRAMAÇÃO**

## 📝 Título do Trabalho

**Mini Sistema de Estoque e Vendas com Estruturas de Dados em Python**

## 👥 Integrantes

* Diego Meira - RA: 1109435
* Vinicius Hoffelder - RA: 1137833
* Kael Fuchs Zatti - RA: 1137819
* Eduardo Barreda Mello - RA: 1138704
* Leonardo Grimm Maziero - RA: 1137914
* Ariel David de Almeida Chaves - RA: 1136093


---

## 💡 Descrição do Sistema

Este projeto consiste no desenvolvimento de um sistema de estoque e vendas executado no terminal, utilizando a linguagem Python.

O sistema permite:

* Cadastro e listagem de clientes
* Cadastro, listagem e busca de produtos
* Realização de vendas
* Visualização do histórico de vendas
* Desfazer a última operação realizada
* Cálculo de valores totais (estoque, vendas e gastos por cliente)

Além disso, o sistema foi projetado com foco em:

* Organização do código utilizando Programação Orientada a Objetos (POO)
* Uso de estruturas de dados clássicas
* Persistência automática dos dados em arquivos

---

## 🧠 Estruturas de Dados Utilizadas

O sistema utiliza três estruturas principais:

### 🔗 Lista Encadeada

Utilizada para armazenar os produtos e/ou clientes.
Permite:

* Inserção de elementos
* Remoção lógica
* Busca
* Listagem

Essa estrutura foi implementada manualmente pelo grupo, sem uso de bibliotecas prontas.

---

### 📥 Fila (Queue)

Utilizada para armazenar as vendas na ordem em que acontecem (FIFO - First In, First Out).

Função:

* Manter o histórico de vendas na ordem correta de processamento

---

### 📚 Pilha (Stack)

Utilizada para armazenar o histórico de operações realizadas.

Função:

* Permitir desfazer a última ação (LIFO - Last In, First Out)

---

## 💾 Persistência Automática em Arquivos

O sistema utiliza arquivos **CSV ou TXT** como forma de armazenamento de dados.

### Funcionamento:

* Ao iniciar o sistema, os dados são carregados automaticamente dos arquivos
* Caso os arquivos não existam, eles são criados automaticamente
* Sempre que ocorre alguma alteração (cadastro, venda, etc.), os dados são salvos automaticamente
* Não existe opção manual de salvar ou carregar dados

### Arquivos utilizados:

* `clientes.csv` ou `clientes.txt`
* `produtos.csv` ou `produtos.txt`
* `vendas.csv` ou `vendas.txt`

### Benefícios:

* Garantia de persistência dos dados
* Continuidade das informações entre execuções
* Sincronização entre memória e arquivos

---

## ▶️ Instruções de Execução

### ✅ Pré-requisitos

* Python 3 instalado na máquina

### 🚀 Passos para executar

1. Clone o repositório:

```bash
git clone <link-do-repositorio>
```

2. Acesse a pasta do projeto:

```bash
cd nome-do-projeto
```

3. Execute o sistema:

```bash
python main.py
```

*(O nome do arquivo principal pode variar)*

---

### 🖥️ Uso do Sistema

Ao executar, será exibido um menu no terminal com opções como:

* Cadastrar cliente
* Cadastrar produto
* Realizar venda
* Listar dados
* Desfazer operação
* Sair

O usuário deve interagir digitando o número correspondente à opção desejada.

---

## ⚠️ Observações

* O sistema possui tratamento de erros para entradas inválidas
* Operações incorretas não afetam os dados salvos
* O sistema nunca encerra abruptamente diante de erros
* Todas as regras de validação são respeitadas (estoque, valores, IDs, etc.)
* Foi solicitado que o algoritmo implementasse apenas funcionalidades mínimas. Entretanto, optamos por incluir uma funcionalidade adicional que separa o processo de reversão de uma operação de venda em etapas distintas: reversão na fila, no cliente e no produto. Essa separação não foi uma escolha de design, mas sim uma necessidade técnica decorrente da arquitetura do sistema. Como cada módulo gerencia seus próprios dados e possui persistência em arquivos separados, não há suporte a transações que agrupem operações relacionadas. Além disso, as classes possuem responsabilidades únicas e não compartilham o estado entre si, o que torna indispensável tratar cada reversão de forma independente.
* O desenvolvimento dos prints de caracteres utilizados para gerar tabelas com linhas e colunas corretamente alinhadas foi realizado com o auxílio de uma inteligência artificial

---

## 🎯 Objetivo do Projeto

Aplicar, na prática:

* Conceitos de Estrutura de Dados
* Programação Orientada a Objetos
* Manipulação de arquivos
* Organização e abstração de código

---

✨ Projeto desenvolvido para fins acadêmicos.
