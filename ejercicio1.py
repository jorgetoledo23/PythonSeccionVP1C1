#Determinar si una persona en base a su edad es Menor, Mayor o Adulto Mayor
#0-17 Menor
#18-65 Mayor
#66+ Adulto Mayor

edad = int(input("Ingrese su Edad: "))

if edad < 18:
    print("menor de edad")
elif edad < 66:
    print("mayor de edad")
else:
    print("adulto mayor")

if edad < 18:
    print("menor de edad")
else:
    if edad < 66:
        print("mayor de edad")
    else:
        print("adulto mayor")

if edad < 18:
    print("Menor")
if edad >= 18 and edad < 66:
    print("Mayor")
if edad > 65:
    print("adulto mayor")