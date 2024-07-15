#3

mi_lista = []
for p in range (10):
  mi_lista.append(int(input("Ingrese un valor: ")))

mayor_primo = mi_lista[0]
posicion_mayor_primo = 0
for i, num in enumerate(mi_lista):
  es_primo = True
  for j in range(2, int(num**0.5) + 1):
    if num % j == 0:
      es_primo = False
      break
  if es_primo and num > mayor_primo:
    mayor_primo = num
    posicion_mayor_primo = i + 1

print(f"El número primo más alto es {mayor_primo} y está en la posición {posicion_mayor_primo}")

