import pytest
import time

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


def test_verificacao_demorada_performance():
    expected = 2
    await_time = 2
    start_time = time.time()
    time.sleep(await_time)
    end_time = time.time()
    duration = int(end_time - start_time)
    assert duration <= expected, f'O teste demorou {duration-expected}seg., mais do que o esperado'