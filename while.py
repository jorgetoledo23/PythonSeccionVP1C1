contador = 0
cantidadNotas = int(input("Ingrese cantidad de Notas a Promediar: "))
suma = 0
while contador < cantidadNotas:
    nota = float(input(f"Ingresa la nota {contador + 1}: "))
    #nota = float(input("Ingresa la nota ", contador, ": ")
    suma += nota
    contador += 1
    #suma = suma + nota
promedio = suma / cantidadNotas
print(f"El Promedio de tus Notas es: {promedio}")