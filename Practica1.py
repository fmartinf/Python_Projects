
print("**************************************************************************")
print("******SISTEMA DE GESTION DE VACACIONES****************")
print("**************************************************************************")
nombre = input ("Introduce tu nombre : ")
clave = int (input("Introduce la clave a la que perteneces: "))
anos = int (input("Introduce los años que llevas en al empresa: "))
if clave == 1 and anos ==1:
                print("Te corresponden "+nombre+ " 6 dias de vacaciones")
elif (clave == 1) and (anos>=2 and  anos<=6):
               print("Te corresponden " + nombre+ " 14 dias de vacaciones")
elif (clave == 1) and (anos>=7):
               print("Te corresponden " + nombre+ " 20 dias de vacaciones")
elif clave == 2 and (anos==1):
               print("Te corresponden " + nombre+ " 7 dias de vacaciones")
elif clave == 2 and (anos>=2 and anos<=6):
               print("Te corresponden " + nombre+ " 15 dias de vacaciones")
elif clave == 2 and (anos>=7):
               print("Te corresponden " + nombre+ " 22 dias de vacaciones")
elif clave == 3 and (anos==1):
               print("Te corresponden " + nombre+ " 10 dias de vacaciones")
elif clave == 3 and (anos>=2 and  anos<=6):
               print("Te corresponden " + nombre+ " 20 dias de vacaciones")
elif clave == 3 and (anos>=7):
               print("Te corresponden " + nombre+ " 30 dias de vacaciones")
elif clave>3:
                print("Error con la clave")
else:
                print("No te corresponden vacaciones, lo siento")
print("FIN")



