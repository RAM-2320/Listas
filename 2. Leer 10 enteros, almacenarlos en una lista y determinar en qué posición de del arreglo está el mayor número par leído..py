#2

mi_lista = []
for p in range (10):
  mi_lista.append(int(input("Ingrese un valor: ")))

mayor_par = mi_lista[0]
posicion_mayor_par = 0
for i, num in enumerate(mi_lista):
  if num % 2 == 0 and num > mayor_par:
    mayor_par = num
    posicion_mayor_par = i + 1

print(f"El número par más alto es {mayor_par} y está en la posición {posicion_mayor_par}")

