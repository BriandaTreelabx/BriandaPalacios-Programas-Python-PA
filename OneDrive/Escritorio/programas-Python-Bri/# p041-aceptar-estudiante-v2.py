# Programa de aceptación de estudiantes en Universidad Kitty Kat SA

nombre = input("Nombre: ")
sexo = input("Sexo (h/m): ").lower()
edad = int(input("Edad: "))

calificaciones = []
for i in range(3):
    cal = float(input(f"Calificación {i+1}: "))
    calificaciones.append(cal)

prom = sum(calificaciones) / 3

if sexo != "m":
    print(f"Lo sentimos, {nombre}. La universidad solo acepta mujeres.")
elif edad <= 21:
    print(f"Lo sentimos, {nombre}. No cumples con la edad requerida (mayores de 21 años).")
elif prom < 8:
    print(f"Lo sentimos, {nombre}. Tu promedio de {prom:.2f} no alcanza el mínimo requerido de 8.")
elif prom > 9.5:
    print(f"Lo sentimos, {nombre}. Tu promedio de {prom:.2f} supera el máximo permitido de 9.5.")
else:
    print(f"¡Felicidades, {nombre}! Has sido aceptada. Cumples con la edad y tu promedio de {prom:.2f} está dentro del rango permitido.")
