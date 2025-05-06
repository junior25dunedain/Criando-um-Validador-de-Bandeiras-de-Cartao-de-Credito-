import re

def identificar_bandeira(numero_cartao):
    # Dicionário com padrões de regex e quantidade correta de dígitos
    padroes_bandeiras = {
        "Visa": (r"^4\d+$", 16),
        "Mastercard": (r"^5[1-5]\d+$", 16),
        "American Express": (r"^3[47]\d+$", 15),
        "Elo": (r"^636\d+$", 16),
        "Diners Club": (r"^3[0689]\d+$", 14),
        "Discover": (r"^6(?:011|5\d{2})\d+$", 16),
        "JCB": (r"^35\d+$", 16)  # Pode ter até 19 dígitos, mas usamos o padrão comum
    }

    # Verificar se a entrada contém apenas números
    if not numero_cartao.isdigit():
        return "Erro: O número do cartão deve conter apenas dígitos."

    # Verificar a bandeira com base no BIN e na quantidade de dígitos esperada
    for bandeira, (padrao, tamanho) in padroes_bandeiras.items():
        if re.match(padrao, numero_cartao) and len(numero_cartao) == tamanho:
            return f"A bandeira do cartão é {bandeira}."

    return "Erro: O número do cartão não corresponde a nenhuma bandeira válida."

# Teste
numero = input("Digite o número do cartão: ")
print(identificar_bandeira(numero))
