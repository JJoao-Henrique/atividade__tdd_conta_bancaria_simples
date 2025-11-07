# Conta Bancária Simples (TDD)

## Como rodar os testes
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
pytest -q

## Estrutura
src/            # código da aplicação
tests/          # testes (pytest)
pytest.ini      # faz o pytest enxergar o pacote src
requirements.txt
