# Identificador de Bandeiras de Cartões de Crédito

## 📌 Introdução
Esta aplicação em Python permite identificar a bandeira de um cartão de crédito com base no número informado pelo usuário. Utilizando expressões regulares, ela verifica o padrão do BIN (Bank Identification Number) e a quantidade correta de dígitos para determinar a bandeira correspondente.

## ⚙️ Funcionamento
A função `identificar_bandeira(numero_cartao)` recebe um número de cartão como entrada e segue os seguintes passos:

1. **Verifica se a entrada contém apenas dígitos**.
2. **Compara o número com padrões de regex** correspondentes às principais bandeiras de cartões.
3. **Confirma se a quantidade de dígitos está correta** para cada bandeira.
4. **Retorna a bandeira identificada ou uma mensagem de erro** caso o número não corresponda a nenhuma bandeira válida.

## 🏷️ Bandeiras Suportadas
O código reconhece as seguintes bandeiras:

- **Visa** (16 dígitos, começa com `4`)
- **Mastercard** (16 dígitos, começa com `51-55`)
- **American Express** (15 dígitos, começa com `34` ou `37`)
- **Elo** (16 dígitos, começa com `636`)
- **Diners Club** (14 dígitos, começa com `30, 36, 38 ou 39`)
- **Discover** (16 dígitos, começa com `6011` ou `65XXX`)
- **JCB** (16 dígitos, começa com `35`, podendo ter até 19 dígitos)

## 🔧 Melhorias Possíveis
Algumas sugestões para aprimorar a aplicação:
- **Permitir números JCB com até 19 dígitos**.
- **Melhorar mensagens de erro**, informando ao usuário possíveis correções.
- **Criar testes automatizados** para validar diferentes números de cartão.
- **Remover espaços ou caracteres extras** antes da verificação.

## 📌 Exemplo de Uso
```python
numero = input("Digite o número do cartão: ")
print(identificar_bandeira(numero))
