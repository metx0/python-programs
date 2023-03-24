secret_number = 777

print(
"""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

guess_number = int(input("Introduce el número: "))

while guess_number != secret_number: # El bucle parará de ejecutarse cuando el número sea igual al número secreto
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    guess_number = int(input("Introduce el número: "))

print("El número secreto es:", secret_number)
print( "¡Bien hecho, muggle! Eres libre ahora.")
