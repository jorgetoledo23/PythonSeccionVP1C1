# Crear un algoritmo en Python que pida al usuario 
# la cantidad de hijos que este tiene. 
# Si es que tiene hijos entonces que ingrese la edad de cada uno 
# y asignar un bono de $25.000 por cada hijo de entre 3 y 15 años. 
# Al final mostrar el total de dinero que obtendría en bono

from validarDatos import *
#from funciones.validarRut import *
#import validarDatos as vD
#import validarDatos

#cantidadNotas = validarInt("Ingrese Cantidad de Notas: ")
#nota = validarFloat("Ingrese su Calificacion: ")

cantidadHijos = validarInt("Ingrese Cantidad de Hijos: ")
if cantidadHijos > 0:
    contador = 1
    totalBono = 0
    while contador <= cantidadHijos:
        edad = validarInt(f"Ingrese la Edad del Hijo N {contador}")
        if edad >= 3 and edad <= 15:
            totalBono += 25000
        else:print("Este Hijo no cumple para el beneficio.")
        contador += 1
    print(f"Usted recibe un beneficio de {totalBono}")
else:print("Como no tiene hijos, no puede optar al beneficio del estado.")