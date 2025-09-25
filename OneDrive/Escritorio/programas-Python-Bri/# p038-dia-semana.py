# Programa que muestra el día de la semana dado un número del 1 al 7

num = int(input("Ingresa un número del 1 al 7: "))

if num == 1:
    print("Domingo")
elif num == 2:
    print("Lunes")
elif num == 3:
    print("Martes")
elif num == 4:
    print("Miércoles")
elif num == 5:
    print("Jueves")
elif num == 6:
    print("Viernes")
elif num == 7:
    print("Sábado")
else:
    print("Error: Día inválido.")
