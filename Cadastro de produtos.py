# =========================================
# SISTEMA DE GERENCIAMENTO DE PRODUTOS
# =========================================

# Lista responsável por armazenar todos os produtos cadastrados
produtos = []


# =========================================
# FUNÇÃO FORMATAR PREÇO
# =========================================

# Função utilizada para formatar os valores monetários trocando ponto por vírgula
def formatar_preco(valor):

    return f"{valor:.2f}".replace(".", ",")

# =========================================
# CLASSE PRODUTO
# =========================================

# Classe responsável por criar objetos do tipo Produto
class Produto:

    # Método construtor da classe
    def __init__(self, nome, categoria, preco, estoque):

        # Atributos privados da classe
        self.__nome = nome
        self.__categoria = categoria.capitalize()

        # Chama os setters para validar os dados
        self.set_preco(preco)
        self.set_estoque(estoque)

    # ---------------------------------
    # GETTERS
    # ---------------------------------

    # Retorna o nome do produto
    def get_nome(self):
        return self.__nome

    # Retorna a categoria do produto
    def get_categoria(self):
        return self.__categoria

    # Retorna o preço do produto
    def get_preco(self):
        return self.__preco

    # Retorna a quantidade em estoque
    def get_estoque(self):
        return self.__estoque

    # ---------------------------------
    # SETTERS
    # ---------------------------------

    # Altera o nome do produto
    def set_nome(self, nome):
        self.__nome = nome

    # Altera a categoria do produto
    def set_categoria(self, categoria):
        self.__categoria = categoria.capitalize()

    # Valida e altera o preço do produto
    def set_preco(self, preco):

        if preco > 0:
            self.__preco = preco

        else:
            print("Preço inválido. O preço deve ser maior que zero.")

    # Valida e altera o estoque do produto
    def set_estoque(self, estoque):

        if estoque >= 0:
            self.__estoque = estoque

        else:
            print("Estoque inválido. O estoque não pode ser negativo.")

    # ---------------------------------
    # MOSTRAR DADOS
    # ---------------------------------

    # Exibe os dados do produto na tela
    def mostrar_dados(self):

        # Calcula o valor total do estoque
        valor_estoque = self.calcular_valor_estoque()

        print(
            f"Produto: {self.__nome} | "
            f"Categoria: {self.__categoria} | "
            f"Preço: R$ {formatar_preco(self.__preco)} | "
            f"Estoque: {self.__estoque} | "
            f"Valor em estoque: R$ {formatar_preco(valor_estoque)}"
        )

    # ---------------------------------
    # CALCULAR VALOR ESTOQUE
    # ---------------------------------

    # Calcula o valor total do produto em estoque
    def calcular_valor_estoque(self):

        return self.__preco * self.__estoque

# =========================================
# CLASSE PRODUTO IMPORTADO
# =========================================

# Classe filha que herda atributos da classe Produto
class ProdutoImportado(Produto):

    # Método construtor da classe ProdutoImportado
    def __init__(self, nome, categoria, preco, estoque, pais_origem):

        # Herda os atributos da classe Produto
        super().__init__(nome, categoria, preco, estoque)

        # Novo atributo da classe filha
        self.__pais_origem = pais_origem

    # ---------------------------------
    # GETTER E SETTER
    # ---------------------------------

    # Retorna o país de origem
    def get_pais_origem(self):
        return self.__pais_origem

    # Altera o país de origem
    def set_pais_origem(self, pais_origem):
        self.__pais_origem = pais_origem

    # ---------------------------------
    # MOSTRAR DADOS
    # ---------------------------------

    # Sobrescreve o método mostrar_dados
    # adicionando o país de origem
    def mostrar_dados(self):

        # Calcula o valor total em estoque
        valor_estoque = self.calcular_valor_estoque()

        print(
            f"Produto: {self.get_nome()} | "
            f"Categoria: {self.get_categoria()} | "
            f"Preço: R$ {formatar_preco(self.get_preco())} | "
            f"Estoque: {self.get_estoque()} | "
            f"País de origem: {self.__pais_origem} | "
            f"Valor em estoque: R$ {formatar_preco(valor_estoque)}"
        )

# =========================================
# FUNÇÃO CADASTRAR PRODUTO
# =========================================

# Função responsável por cadastrar novos produtos
def cadastrar_produto():

    print("\n===== CADASTRAR PRODUTO =====")

    # Recebe o nome e categoria do produto
    nome = input("Digite o nome do produto: ").capitalize()

    categoria = input(
        "Digite a categoria do produto: "
    ).capitalize()

    # ---------------------------------
    # VALIDAÇÃO DO PREÇO
    # ---------------------------------

    while True:

        try:

            # Recebe o preço digitado pelo usuário
            preco = float(input("Digite o preço do produto: R$ ").replace(",", "."))

            # Verifica se o preço é válido
            if preco > 0:
                break

            else:
                print("Preço inválido. O preço deve ser maior que 0.")

        except:

            print("Digite um preço válido.")

    # ---------------------------------
    # VALIDAÇÃO DO ESTOQUE
    # ---------------------------------

    while True:

        try:

            # Recebe a quantidade em estoque
            estoque = int(input("Digite a quantidade em estoque: "))

            # Verifica se o estoque é válido
            if estoque >= 0:
                break

            else:
                print("Estoque inválido. O estoque não pode ser negativo.")

        except:

            print("Digite uma quantidade válida.")

    # ---------------------------------
    # VALIDAÇÃO DE PRODUTO IMPORTADO
    # ---------------------------------

    while True:

        # Pergunta se o produto é importado
        resposta = input(
            "O produto é importado? (s/n): "
        ).strip().lower()

        # ---------------------------------
        # CADASTRO DE PRODUTO IMPORTADO
        # ---------------------------------

        if resposta in ["s", "sim"]:

            # Validação do país de origem
            while True:

                pais_origem = input("Digite o país de origem: " ).strip().title()

                # Verifica se o país contém apenas letras
                if pais_origem.replace(" ", "").replace("-", "").isalpha():

                    produto = ProdutoImportado(
                        nome,
                        categoria,
                        preco,
                        estoque,
                        pais_origem
                    )

                    # Adiciona o produto na lista
                    produtos.append(produto)

                    print("\nProduto cadastrado com sucesso!")

                    break
                
                #Se usuario digitar um nome de país invalido com digitos ou caractere
                else:

                    print("Nome de país invalido")

            break

        # ---------------------------------
        # CADASTRO DE PRODUTO NACIONAL
        # ---------------------------------

        elif resposta in ["n", "nao", "não"]:

            produto = Produto(
                nome,
                categoria,
                preco,
                estoque
            )

            # Adiciona o produto na lista
            produtos.append(produto)

            print("\nProduto cadastrado com sucesso!")

            break

        # OPÇÃO INVÁLIDA
        else:

            print("Opção inválida. Digite apenas S ou N.")

# =========================================
# FUNÇÃO LISTAR PRODUTOS
# =========================================

# Função responsável por listar os produtos cadastrados
def listar_produtos():

    print("\n===== PRODUTOS CADASTRADOS =====")

    # Verifica se existem produtos cadastrados
    if len(produtos) == 0:

        print("Nenhum produto cadastrado.")
        return

    # Percorre a lista mostrando os produtos
    for produto in produtos:

        produto.mostrar_dados()

# =========================================
# FUNÇÃO MOSTRAR RELATÓRIO
# =========================================

# Função responsável por gerar os relatórios do sistema
def mostrar_relatorio():

    print("\n===== RELATÓRIO FINAL =====")

    # Verifica se existem produtos cadastrados
    if len(produtos) == 0:

        print("Nenhum produto cadastrado.")
        return

    # Variáveis utilizadas nos cálculos
    total_estoque = 0
    soma_precos = 0

    # Define inicialmente o primeiro produto
    # como mais caro e mais barato
    produto_mais_caro = produtos[0]
    produto_mais_barato = produtos[0]

    # ---------------------------------
    # PERCORRER LISTA DE PRODUTOS
    # ---------------------------------

    for produto in produtos:

        # Soma o valor total do estoque
        total_estoque += produto.calcular_valor_estoque()

        # Soma os preços dos produtos
        soma_precos += produto.get_preco()

        # Verifica o produto mais caro
        if produto.get_preco() > produto_mais_caro.get_preco():

            produto_mais_caro = produto

        # Verifica o produto mais barato
        if produto.get_preco() < produto_mais_barato.get_preco():

            produto_mais_barato = produto

    # Calcula a média de preços
    media_precos = soma_precos / len(produtos)

    # ---------------------------------
    # DICIONÁRIO DO RELATÓRIO
    # ---------------------------------

    relatorio = {

        "quantidade_produtos": len(produtos),
        "media_precos": media_precos,
        "produto_mais_caro": produto_mais_caro,
        "produto_mais_barato": produto_mais_barato,
        "valor_total_estoque": total_estoque
    }

    # ---------------------------------
    # MOSTRAR PRODUTOS
    # ---------------------------------

    for produto in produtos:

        produto.mostrar_dados()

    # ---------------------------------
    # MOSTRAR DADOS DO RELATÓRIO
    # ---------------------------------

    print(f"\nQuantidade de produtos: {relatorio['quantidade_produtos']}")

    print(
        f"Média de preços: "
        f"R$ {formatar_preco(relatorio['media_precos'])}"
    )

    print(
        f"Produto mais caro: "
        f"{relatorio['produto_mais_caro'].get_nome()} - "
        f"R$ {formatar_preco(relatorio['produto_mais_caro'].get_preco())}"
    )

    print(
        f"Produto mais barato: "
        f"{relatorio['produto_mais_barato'].get_nome()} - "
        f"R$ {formatar_preco(relatorio['produto_mais_barato'].get_preco())}"
    )

    print(
        f"Valor total em estoque: "
        f"R$ {formatar_preco(relatorio['valor_total_estoque'])}"
    )

# =========================================
# MENU PRINCIPAL
# =========================================

# Estrutura principal do sistema
while True:

    print("""
===============================
            MENU
===============================
1 - Cadastrar produto
2 - Listar produtos
3 - Mostrar relatório
4 - Sair
===============================
""")

    # Recebe a opção escolhida pelo usuário
    opcao = input("Escolha uma opção: ").lower()

    # OPÇÃO 1 - CADASTRAR PRODUTO
    if opcao == "1":

        cadastrar_produto()

    # OPÇÃO 2 - LISTAR PRODUTOS
    elif opcao == "2":

        listar_produtos()

    # OPÇÃO 3 - MOSTRAR RELATÓRIO
    elif opcao == "3":

        mostrar_relatorio()

    # OPÇÃO 4 - SAIR
    elif opcao == "4":

        print("\nPrograma encerrado.")
        break

    # OPÇÃO INVÁLIDA
    else:

        print("Opção inválida. Escolha uma opção válida.")
        
