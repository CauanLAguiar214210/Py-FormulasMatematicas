def calcular_valor_absoluto(numero):
    if numero < 0:
        return -numero
    else:
        return numero

# Exemplo de uso
numero = float(input("Digite um número: "))

valor_absoluto = calcular_valor_absoluto(numero)

print("O valor absoluto de", numero, "é:", valor_absoluto)