def calcular_vertice(a, b, c):
    # Fórmula para calcular as coordenadas do vértice (h, k)
    h = -b / (2*a)
    k = (4*a*c - b**2) / (4*a)

    return h, k

# Exemplo de uso
coeficiente_a = float(input("Digite o coeficiente a: "))
coeficiente_b = float(input("Digite o coeficiente b: "))
coeficiente_c = float(input("Digite o coeficiente c: "))

vertice = calcular_vertice(coeficiente_a, coeficiente_b, coeficiente_c)

print("As coordenadas do vértice são:", vertice)