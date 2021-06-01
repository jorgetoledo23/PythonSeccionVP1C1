#Crear funcionalidad de solo aceptar Si o No. 
while True:    
    opcion = input("Escriba Si para Continuar, No para salir! ")
    opcionMayuscula = opcion.upper()
    if opcionMayuscula == "SI":
        #break
        #Hacer las intrucciones para cuando ingresa SI
        print("")
    elif opcionMayuscula == "NO":
        #Hacer las intrucciones para cuando ingresa NO
        break
    else:
        print("El Dato ingresado NO es valido!")
print("Gracias!")




