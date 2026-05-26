# Lista que armazena os produtos cadastrados
produtos = []

# =========================================
# FORMATAR PREÇO
# =========================================

def formatar_preco(valor):
    return f"{valor:.2f}".replace(".", ",")

# =========================================
# CLASSE PRODUTO
# =========================================

class Produto:

    def __init__(self, nome, categoria, preco, estoque):

        self.__nome = nome
        self.__categoria = categoria.capitalize()

        self.set_preco(preco)
        self.set_estoque(estoque)

    # =========================
    # GETTERS
    # =========================

    def get_nome(self):
        return self.__nome

    def get_categoria(self):
        return self.__categoria

    def get_preco(self):
        return self.__preco

    def get_estoque(self):
        return self.__estoque

    # =========================
    # SETTERS
    # =========================

    def set_preco(self, preco):

        if preco > 0:
            self.__preco = preco

        else:
            print("Preço inválido.")

    def set_estoque(self, estoque):

        if estoque >= 0:
            self.__estoque = estoque

        else:
            print("Estoque inválido.")

    # =========================
    # MOSTRAR DADOS
    # =========================

    def mostrar_dados(self):

        valor_estoque = self.calcular_valor_estoque()

        print(
            f"Produto: {self.__nome} | "
            f"Categoria: {self.__categoria} | "
            f"Tipo: Nacional | "
            f"Preço: R$ {formatar_preco(self.__preco)} | "
            f"Estoque: {self.__estoque} | "
            f"Valor em estoque: R$ {formatar_preco(valor_estoque)}"
        )

    # =========================
    # CALCULAR ESTOQUE
    # =========================

    def calcular_valor_estoque(self):
        return self.__preco * self.__estoque


# =========================================
# CLASSE PRODUTO IMPORTADO
# =========================================

class ProdutoImportado(Produto):

    def __init__(self, nome, categoria, preco, estoque, pais_origem):

        super().__init__(
            nome,
            categoria,
            preco,
            estoque
        )

        self.__pais_origem = pais_origem

    # =========================
    # GETTER
    # =========================

    def get_pais_origem(self):
        return self.__pais_origem

    # =========================
    # MOSTRAR DADOS
    # =========================

    def mostrar_dados(self):

        valor_estoque = self.calcular_valor_estoque()

        print(
            f"Produto: {self.get_nome()} | "
            f"Categoria: {self.get_categoria()} | "
            f"Tipo: Importado | "
            f"País: {self.__pais_origem} | "
            f"Preço: R$ {formatar_preco(self.get_preco())} | "
            f"Estoque: {self.get_estoque()} | "
            f"Valor em estoque: R$ {formatar_preco(valor_estoque)}"
        )


# =========================================
# CADASTRAR PRODUTO
# =========================================

def cadastrar_produto():

    print("\n===== CADASTRAR PRODUTO =====")

    # =========================
    # NOME
    # =========================

    while True:

        nome = input(
            "Digite o nome do produto: "
        ).strip().title()

        if nome != "":
            break

        print("Nome inválido.")

    # =========================
    # CATEGORIA
    # =========================

    while True:

        categoria = input(
            "Digite a categoria do produto: "
        ).strip().title()

        if categoria != "":
            break

        print("Categoria inválida.")

    # =========================
    # PREÇO
    # =========================

    while True:

        try:

            preco = float(
                input(
                    "Digite o preço do produto: R$ "
                ).replace(",", ".")
            )

            if preco > 0:
                break

            print("Preço inválido.")

        except:
            print("Digite um preço válido.")

    # =========================
    # ESTOQUE
    # =========================

    while True:

        try:

            estoque = int(
                input(
                    "Digite a quantidade em estoque: "
                )
            )

            if estoque >= 0:
                break

            print("Estoque inválido.")

        except:
            print("Digite uma quantidade válida.")

    # =========================
    # IMPORTADO?
    # =========================

    while True:

        resposta = input(
            "O produto é importado? (s/n): "
        ).strip().lower()

        # =====================================
        # PRODUTO IMPORTADO
        # =====================================

        if resposta in ["s", "sim"]:

            while True:

                pais_origem = input(
                    "Digite o país de origem: "
                ).strip().title()

                if pais_origem.replace(" ", "").replace("-", "").isalpha():
                    break

                print("País inválido.")

            # =========================
            # VERIFICAR DUPLICADOS
            # =========================

            for produto in produtos:

                if isinstance(produto, ProdutoImportado):

                    if (
                        produto.get_nome().lower() == nome.lower()
                        and
                        produto.get_categoria().lower() == categoria.lower()
                        and
                        produto.get_pais_origem().lower() == pais_origem.lower()
                    ):

                        produto.set_estoque(
                            produto.get_estoque() + estoque
                        )

                        print(
                            "\nProduto importado já existente."
                        )

                        print(
                            "Estoque atualizado com sucesso!"
                        )

                        return

            # =========================
            # CADASTRAR IMPORTADO
            # =========================

            produto = ProdutoImportado(
                nome,
                categoria,
                preco,
                estoque,
                pais_origem
            )

            produtos.append(produto)

            print("\nProduto importado cadastrado com sucesso!")

            return

        # =====================================
        # PRODUTO NACIONAL
        # =====================================

        elif resposta in ["n", "nao", "não"]:

            # =========================
            # VERIFICAR DUPLICADOS
            # =========================

            for produto in produtos:

                if not isinstance(produto, ProdutoImportado):

                    if (
                        produto.get_nome().lower() == nome.lower()
                        and
                        produto.get_categoria().lower() == categoria.lower()
                    ):

                        produto.set_estoque(
                            produto.get_estoque() + estoque
                        )

                        print(
                            "\nProduto nacional já existente."
                        )

                        print(
                            "Estoque atualizado com sucesso!"
                        )

                        return

            # =========================
            # CADASTRAR NACIONAL
            # =========================

            produto = Produto(
                nome,
                categoria,
                preco,
                estoque
            )

            produtos.append(produto)

            print("\nProduto nacional cadastrado com sucesso!")

            return

        else:
            print("Digite apenas S ou N.")


# =========================================
# LISTAR PRODUTOS
# =========================================

def listar_produtos():

    print("\n===== PRODUTOS CADASTRADOS =====")

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    for produto in produtos:
        produto.mostrar_dados()


# =========================================
# RELATÓRIO
# =========================================

def mostrar_relatorio():

    print("\n===== RELATÓRIO FINAL =====")

    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return

    total_estoque = 0
    soma_precos = 0

    produto_mais_caro = produtos[0]
    produto_mais_barato = produtos[0]

    # =========================
    # PERCORRER LISTA
    # =========================

    for produto in produtos:

        total_estoque += produto.calcular_valor_estoque()

        soma_precos += produto.get_preco()

        if produto.get_preco() > produto_mais_caro.get_preco():
            produto_mais_caro = produto

        if produto.get_preco() < produto_mais_barato.get_preco():
            produto_mais_barato = produto

    # =========================
    # MÉDIA
    # =========================

    media_precos = soma_precos / len(produtos)

    # =========================
    # MOSTRAR PRODUTOS
    # =========================

    for produto in produtos:
        produto.mostrar_dados()

    # =========================
    # RELATÓRIO FINAL
    # =========================

    print(
        f"\nQuantidade de produtos: {len(produtos)}"

        f"\nMédia de preços: "
        f"R$ {formatar_preco(media_precos)}"

        f"\nProduto mais caro: "
        f"{produto_mais_caro.get_nome()} - "
        f"R$ {formatar_preco(produto_mais_caro.get_preco())}"

        f"\nProduto mais barato: "
        f"{produto_mais_barato.get_nome()} - "
        f"R$ {formatar_preco(produto_mais_barato.get_preco())}"

        f"\nValor total em estoque: "
        f"R$ {formatar_preco(total_estoque)}"
    )


# =========================================
# MENU PRINCIPAL
# =========================================

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

    opcao = input(
        "Escolha uma opção: "
    ).strip()

    # =========================
    # CADASTRAR
    # =========================

    if opcao == "1":
        cadastrar_produto()

    # =========================
    # LISTAR
    # =========================

    elif opcao == "2":
        listar_produtos()

    # =========================
    # RELATÓRIO
    # =========================

    elif opcao == "3":
        mostrar_relatorio()

    # =========================
    # SAIR
    # =========================

    elif opcao == "4":

        print("\nPrograma encerrado.")
        break

    # =========================
    # OPÇÃO INVÁLIDA
    # =========================

    else:
        print("\nEscolha uma opção válida.")
