print("Evaluación del curso")
nombre = input ("Cual es tu nombre: ")
nota1 = float (input("Introduce la nota de Matematicas: "))
nota2 = float (input("Introduce la nota de Catalan: "))
nota3 = float (input("Introduce la nota de Historia: "))
media = (nota1+nota2+nota3)/3
if media>=5:
    print ("Aprobado con la nota " + str(media))
print("Suspenso")
