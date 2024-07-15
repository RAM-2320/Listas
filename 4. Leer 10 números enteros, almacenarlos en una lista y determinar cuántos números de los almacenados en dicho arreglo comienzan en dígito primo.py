#4

mi_lista = []
for p in range (10):
  mi_lista.append(int(input("Ingrese un valor: ")))

cantidad_primos = 0
for num in mi_lista:
  primer_digito = int(str(num)[0])
  es_primo = True
  for j in range(2, int(primer_digito**0.5) + 1):
    if primer_digito % j == 0:
      es_primo = False
      break
  if es_primo:
    cantidad_primos += 1

print(f"Hay {cantidad_primos} números en la lista que comienzan con un dígito primo.")

