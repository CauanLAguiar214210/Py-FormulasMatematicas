def calcular_valor_polinomial(coeficientes, x):
    grau = len(coeficientes) - 1
    valor_polinomial = 0

    for i, coeficiente in enumerate(coeficientes):
        valor_polinomial += coeficiente * (x ** (grau - i))

    return valor_polinomial

# Exemplo de uso
coeficientes = [float(c) for c in input("Digite os coeficientes do polinômio, separados por espaço: ").split()]
valor_x = float(input("Digite o valor de x: "))

valor_polinomial = calcular_valor_polinomial(coeficientes, valor_x)

print("O valor do polinômio para x =", valor_x, "é:", valor_polinomial)