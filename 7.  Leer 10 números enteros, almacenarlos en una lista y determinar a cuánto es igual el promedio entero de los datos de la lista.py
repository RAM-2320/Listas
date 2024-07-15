#7

numeros = []

for i in range(10):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

promedio = sum(numeros) // len(numeros)

print("El promedio entero de los datos de la lista es:", promedio)
