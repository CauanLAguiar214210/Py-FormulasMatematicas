import math

def calcular_cosseno(angulo):
    valor_cosseno = math.cos(math.radians(angulo))
    return valor_cosseno

# Exemplo de uso
angulo = float(input("Digite o ângulo em graus: "))

valor_cosseno = calcular_cosseno(angulo)

print("O valor do cosseno para o ângulo", angulo, "é:", valor_cosseno)