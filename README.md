
# Pytest CI/CD

### Fazendo CI/CD no Github Actions usando Pytest.
## 📘 Sobre este repositório:
Estudo de uso do Pytest com simples testes de Integração e testes Unitários.  
Criar um Workflow de CI/CD no Github Actions de forma a permitir ao observador analisar as etapas e verificar os casos de sucesso dos testes para aprovação ou não do código e da pull request.

## 🛠️ Ferramentas utilizadas:
| Ferramenta |URL |
|-------|--------|
| Python 3.12 | [🔗Link]('https://www.python.org/downloads/release/python-3120/')
| Poetry 1.8.3 | [🔗Link]('https://pypi.org/project/poetry/')
| Pytest 8.3.2 | [🔗Link]('https://pypi.org/project/pytest/')
| Pytest-cov 5.0.0 | [🔗Link]('https://pypi.org/project/pytest-cov/')
| Pytest-asyncio 0.24.0 | [🔗Link]('https://pypi.org/project/pytest-asyncio/')
| Ruff 0.6.3 | [🔗Link]('https://pypi.org/project/ruff/')
| Taskipy 1.13.0 | [🔗Link]('https://pypi.org/project/taskipy/')


## 🛠️ Clonando este repositório:
```bash
git clone https://github.com/devfabiopedro/pytestCICD.git
```

1. Vá para dentro do diretório da aplicação:
```
cd\pytestCICD
```

2. Crie um ambiente virtual com o Poetry:
```
poetry shell
```

3. Instale as dependências do projeto:
```
poetry install
```

## 🚀 Uso:
O Taskipy é uma biblioteca Python que facilita a criação e execução de tarefas de automação.  
Neste estudo usei o [Taskipy](https://pypi.org/project/taskipy/) para facilitar a execução de linhas de comandos. 

No console do seu sistema operacional ou console do seu editor, execute o comando:
```
task --list
```
Isso vai listar todos os comandos disponíveis para: Linter, Formatar, Testar e Gerar Documentação de Cobertura de Testes:
```
     lint ➡️ Faz checagem lint no código.
   format ➡️ Formata o código corretamente.
     test ➡️ Executa os testes.
post-test ➡️ Exibe relatório de cobertura dos testes.
```

Voce também poderá executar os testes utilizando marcadores disponíveis:
```
task test -m integracao ➡️ Executa só os Testes de Integração.
task test -m unitario   ➡️ Executa só os Testes Unitarios.
```

## 👋😃 Obrigado por visitar