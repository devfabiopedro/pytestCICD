import pytest

# Testes unitários do métodos de classe Estoque e Produto
# Verificando se os resultados funcionam como deveriam.


@pytest.mark.unitario
def test_criar_um_produto(produto):
    assert produto == {'nome': 'Notebook', 'qtde': 1}


@pytest.mark.unitario
def test_entrada_de_produto_em_estoque(estoque):
    assert estoque == {'Impressora HP': 50}


@pytest.mark.unitario
def test_verificar_se_tem_estoque(estoque):
    valor_esperado = 50
    assert estoque['Impressora HP'] == valor_esperado
