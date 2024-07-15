#5

nums = []
for _ in range(10):
  nums.append(int(input("Ingrese un valor: ")))

pos_max_pares = -1
max_pares = 0
for i, num in enumerate(nums):
  primo = True
  for j in range(2, int(num**0.5) + 1):
    if num % j == 0:
      primo = False
      break
  if primo:
    pares = 0
    for digito in str(num):
      if int(digito) % 2 == 0:
        pares += 1
    if pares > max_pares:
      max_pares = pares
      pos_max_pares = i

print(f"El número primo con mayor cantidad de dígitos pares esta en la posición {pos_max_pares}")

