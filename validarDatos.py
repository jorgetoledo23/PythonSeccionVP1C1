def validarInt(mensaje):
    while True:
        try:
            datoInt = int(input(mensaje))
            break
        except:
            print("Dato NO Valido!")
    return datoInt        

def validarFloat(mensaje):
    while True:
        try:
            datoFloat = float(input(mensaje))
            break
        except:
            print("Dato NO Valido!")
    return datoFloat