
'''
Pequena aplicação que ajuda a simular nos testes de integração
'''


# Parte da aplicação que cria Produtos
class Produto:
    def __init__(self, nome: str, qtde: int) -> None:
        self.nome: str = nome
        self.qtde: int = qtde


# Parte da aplicação que gerencia Estoque
class Estoque:
    def __init__(self) -> None:
        self.produtos: dict = {}

    def adicionar_produto(self, produto: str) -> str:
        if produto.nome not in self.produtos:
            self.produtos[produto.nome] = produto.qtde
        else:
            self.produtos[produto.nome] += produto.qtde

    def verifica_quantidade(self, nome_produto: str) -> str:
        return self.produtos.get(nome_produto, 0)
