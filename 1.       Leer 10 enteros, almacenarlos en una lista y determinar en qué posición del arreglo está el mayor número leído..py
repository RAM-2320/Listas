#1

mi_lista = []
for p in range (10):
  mi_lista.append(int(input("Ingrese un valor: ")))

numero_mayor = mi_lista[0]
posicion_mayor = 0
for i, num in enumerate(mi_lista):
  if num > numero_mayor:
    numero_mayor = num
    posicion_mayor = i + 1

print(f"El número más alto es {numero_mayor} y está en la posición {posicion_mayor}")

