# Programa que calcula el promedio de 5 calificaciones

notas = []
for i in range(5):
    nota = float(input(f"Ingrese la calificación {i+1}: "))
    notas.append(nota)

prom = sum(notas) / 5

print(f"Tu promedio es {prom:.2f}. ", end="")

if prom < 6:
    print("Quedas reprobado")
elif prom < 7:
    print("Pasas de panzazo")
elif prom < 8:
    print("Muy bien, puedes mejorar")
elif prom < 9:
    print("Excelente, sigue así")
else:
    print("Perfecto, tu esfuerzo valió la pena")
