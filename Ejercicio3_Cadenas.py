
print("Concatenacion------------")
mensaje= "Hola"
mensaje += " "
mensaje += "esto es una concatenacion"
print(mensaje)

num1=1
num2=45
suma=num1+num2
suma =str(suma)
print("El resultado es: "+suma )

print("Subcadena------------")
buscar_subcadena=mensaje.find("concatenacion")
#Indica la posiicion a partir de donde se encuentra
print(buscar_subcadena)

print("Extraccion------------")
print(mensaje+" " +"Este es el mensaje")
extraer_cadena=mensaje[5:12]
print(extraer_cadena)

print("Comparacion------------")
mens1="Ferran"
mens2="Fernando"
print(mens1==mens2)

