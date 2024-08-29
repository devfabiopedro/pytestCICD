import pytest

from app.main import Estoque, Produto

# Testes de Integração usando a aplicação de Produtos e Estoque
# E verificando se o resultado dessa integração funciona como deveria.


@pytest.mark.integracao
def test_adicionar_produto_e_verificar_quantidade_no_estoque():
    estoque = Estoque()

    qtde = [10, 5]
    produto1 = Produto('Mouse', qtde[0])
    produto2 = Produto('Teclado', qtde[1])
    # Adicionar 2 tipos de produtos diferentes
    estoque.adicionar_produto(produto1)
    estoque.adicionar_produto(produto2)

    assert estoque.verifica_quantidade('Mouse') == qtde[0]
    assert estoque.verifica_quantidade('Teclado') == qtde[1]


@pytest.mark.integracao
def test_adicionar_produto_existente_e_verificar_se_estoque_e_somado():
    estoque = Estoque()

    qtde = [14, 8]
    estoque_somado_esperado = 22

    # Adicionar 2 tipos de produtos iguais
    produto1 = Produto('Mouse', qtde[0])
    estoque.adicionar_produto(produto1)

    produto2 = Produto('Mouse', qtde[1])
    estoque.adicionar_produto(produto2)

    assert estoque.verifica_quantidade('Mouse') == estoque_somado_esperado
