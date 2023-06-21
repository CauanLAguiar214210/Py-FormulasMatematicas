def calcular_valor_afim(a, b, x):
    y = a * x + b
    return y

# Exemplo de uso
coeficiente_a = float(input("Digite o coeficiente a: "))
coeficiente_b = float(input("Digite o coeficiente b: "))
valor_x = float(input("Digite o valor de x: "))

valor_y = calcular_valor_afim(coeficiente_a, coeficiente_b, valor_x)

print("O valor de y é:", valor_y)