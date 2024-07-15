#10

numeros = []

for _ in range(10):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

numero_a_dividir = int(input("Ingrese el número para verificar divisores: "))

divisores_exactos = sum(1 for numero in numeros if numero_a_dividir % numero == 0)

print("Cantidad de divisores exactos en la lista:", divisores_exactos)


