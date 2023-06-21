import math

def calcular_logaritmo(numero, base):
    resultado = math.log(numero, base)
    return resultado

# Exemplo de uso
numero = float(input("Digite um número: "))
base = float(input("Digite a base do logaritmo: "))

valor_logaritmo = calcular_logaritmo(numero, base)

print("O logaritmo de", numero, "na base", base, "é:", valor_logaritmo)