import pytest

from app.main import Estoque, Produto


def to_json(produto: Produto) -> dict:
    return {'nome': produto.nome, 'qtde': produto.qtde}


@pytest.fixture
def produto():
    novo_produto = to_json(Produto('Notebook', 1))
    return novo_produto


@pytest.fixture
def estoque():
    obj_estoque = Estoque()
    obj_produto = Produto('Impressora HP', 50)
    obj_estoque.adicionar_produto(obj_produto)
    return obj_estoque.produtos
