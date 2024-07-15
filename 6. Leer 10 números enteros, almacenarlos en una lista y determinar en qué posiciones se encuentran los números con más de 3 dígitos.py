#6

numeros = []

for _ in range(10):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

promedio = sum(numeros) // len(numeros)

print("El promedio entero de los datos de la lista es:", promedio)