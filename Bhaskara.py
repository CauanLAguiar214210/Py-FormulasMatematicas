import math

def calcular_raizes(a, b, c):
    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
        return raiz1, raiz2
    elif discriminante == 0:
        raiz = -b / (2*a)
        return raiz
    else:
        return "Não há raízes reais."

# Exemplo de uso
coeficiente_a = float(input("Digite o coeficiente a: "))
coeficiente_b = float(input("Digite o coeficiente b: "))
coeficiente_c = float(input("Digite o coeficiente c: "))

raizes = calcular_raizes(coeficiente_a, coeficiente_b, coeficiente_c)

print("As raízes são:", raizes)