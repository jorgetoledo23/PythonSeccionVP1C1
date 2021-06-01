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



semaforo = True
#while semaforo == True:
while semaforo:
    try:
        edad = int(input("Ingresa tu Edad: "))
        semaforo = False
    except:
        print("El Dato ingresado NO es valido!")
print("Dato Correcto!")

#Ingresando Notas (Solo sean validos los Numeros del 1 al 7)
while True:
    #Cualquiear se ejecute siempre
    try:
        nota = float(input("Ingrese una Nota: "))
        if nota >= 1 and nota <=7:
           break
        else:
            print("La nota debe estar entre 1 y 7")
    except:
        print("Nota ingresada NO VALIDA!")
print("Nota Correcta!")

semaforo = True
#while semaforo == True:
while semaforo:
    try:
        nota = float(input("Ingresa tu Nota: "))
        if nota >= 1 and nota <= 7:
            semaforo = False
        else:
            print("La nota debe estar entre 1 y 7")
    except:
        print("El Dato ingresado NO es valido!")
print("Nota Correcto!")


