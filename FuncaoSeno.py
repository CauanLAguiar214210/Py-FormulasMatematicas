import math

def calcular_valor_seno(angulo):
    valor_seno = math.sin(math.radians(angulo))
    return valor_seno

# Exemplo de uso
angulo = float(input("Digite o ângulo em graus: "))

valor_seno = calcular_valor_seno(angulo)

print("O valor do seno para o ângulo", angulo, "é:", valor_seno)