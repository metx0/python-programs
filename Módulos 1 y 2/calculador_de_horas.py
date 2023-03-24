horas = int(input("Hora de inicio (horas): "))
mins = int(input("Minuto de inicio (minutos): "))
duracion = int(input("Duración del evento (minutos) "))

mins = mins + duracion #Obtenemos los minutos totales
horas = horas + mins // 60 #Obtenemos las horas totales
mins %= 60
horas %= 24

print(horas, ":", mins, sep = '')