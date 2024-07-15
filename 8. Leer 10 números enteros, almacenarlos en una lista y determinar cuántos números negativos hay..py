#8

numeros = []

for _ in range(10):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

negativos = sum(1 for numero in numeros if numero < 0)

print("Cantidad de números negativos:", negativos)

