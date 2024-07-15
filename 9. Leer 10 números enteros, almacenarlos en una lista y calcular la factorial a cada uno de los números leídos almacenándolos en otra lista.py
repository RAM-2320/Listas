#9

numeros = []
factoriales = []

for _ in range(10):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    factoriales.append(factorial)

print("Lista de factoriales:", factoriales)

