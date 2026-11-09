# Atividade 4: Testes Automatizados do LocalEats

## Identificação

- Unidade curricular: Qualidade de Software
- Projeto: LocalEats
- Modalidade: individual
- Responsável: Marco
- Sistema: [LocalEats](https://local-eats-unisenac.vercel.app/)

## Regra unitária e TDD

**Regra escolhida:** verificar se o pedido atingiu o valor mínimo de R$ 30,00.

A função `pedido_atingiu_valor_minimo(valor_pedido)` retorna `True` para pedidos de R$ 30,00 ou mais, `False` para valores menores e lança `ValueError` para valores negativos.

**Primeiro teste escrito:** `test_pedido_no_valor_minimo_e_aceito`, para verificar o limite de R$ 30,00.

**Por que o teste falhou inicialmente:** a primeira execução ocorreu antes da implementação e falhou na coleta porque a função ainda não existia no módulo.

**Implementação mínima realizada:** rejeitar valores negativos com `ValueError` e comparar os demais valores com o mínimo de 30.

**Segundo teste escrito:** `test_pedido_abaixo_do_minimo_nao_e_aceito`, para verificar o comportamento abaixo do limite. Também foi incluído o caso adicional `test_valor_negativo_gera_value_error`.

**Melhoria ou refatoração realizada:** manter a validação do valor negativo antes da comparação do pedido, deixando explícita a regra da exceção.

## Teste funcional com Playwright

O teste `test_tela_de_login_permite_abrir_cadastro` acessa a tela de login do LocalEats, verifica que o campo de e-mail está visível e clica em “Criar Conta”. As assertions confirmam que o campo de nome e o botão “Registrar” aparecem. O teste usa locators do Playwright, não utiliza espera fixa e não envia o formulário nem cria uma conta.

## Identificação dos testes

| ID | Integrante | Tipo | Comportamento verificado | Arquivo e função |
|---|---|---|---|---|
| TU01 | Marco | Unitário | Pedido exatamente no valor mínimo é aceito | `tests/test_regras_localeats.py::test_pedido_no_valor_minimo_e_aceito` |
| TU02 | Marco | Unitário | Pedido abaixo do valor mínimo não é aceito | `tests/test_regras_localeats.py::test_pedido_abaixo_do_minimo_nao_e_aceito` |
| TU03 | Marco | Unitário | Valor negativo gera `ValueError` | `tests/test_regras_localeats.py::test_valor_negativo_gera_value_error` |
| TF01 | Marco | Funcional | Abertura do formulário de cadastro pela tela de login | `tests/test_localeats.py::test_tela_de_login_permite_abrir_cadastro` |

## Execução

Na pasta `atividade04`, instale as dependências e o navegador do Playwright:

```bash
python -m pip install -r requirements.txt
python -m playwright install --with-deps chromium
```

Execute toda a suíte e atualize o relatório:

```bash
python -m pytest -v | tee relatorio-pytest.txt
```