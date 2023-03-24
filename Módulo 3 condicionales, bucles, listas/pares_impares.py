pares = 0
impares = 0

num = int(input("Escriba el número a comparar o escriba 0 para terminar: "))

while num != 0: #El bucle se para de ejecutar cuando el número escrito es igual a 0
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    num = int(input("Escriba el número a comparar o escriba 0 para terminar: "))

print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)



