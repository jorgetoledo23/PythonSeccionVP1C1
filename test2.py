# Crear un algoritmo en Python que pida al usuario 
# la cantidad de hijos que este tiene. 
# Si es que tiene hijos entonces que ingrese la edad de cada uno 
# y asignar un bono de $25.000 por cada hijo de entre 3 y 15 años. 
# Al final mostrar el total de dinero que obtendría en bono

from validarDatos import *

cantidadHijos = validarInt("Ingrese Cantidad de Hijos: ")
totalBono = 0

if cantidadHijos > 0:
    for i in range(cantidadHijos):
        edad = validarInt(f"Ingresa la Edad del hijo N {i + 1}: ")
        if (edad >= 3 and edad <= 15):
            #Asigna BONO
            totalBono += 25000
        else:print("Para este hijo no cumple los requisitos")
    print(f"El total que obtienes por concepto de BONO es: {totalBono}")
else: print("Como no tienes hijos, NO puedes optar al Beneficio.")

