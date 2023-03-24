n = int(input("Escriba el número: "))
steps = 0

while n > 1:
    if n % 2 == 0:
        while n % 2 == 0:
            n //= 2
            print(n)
            steps += 1
    else:
        n = n * 3 + 1
        print(n)
        steps += 1

print("\nNúmero de pasos:", steps)



    
