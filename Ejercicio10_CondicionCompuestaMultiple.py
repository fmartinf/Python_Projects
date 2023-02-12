print("Verificar si un numero es multiplo de otro")
num1 = float(input ("Introduce un numero : "))
num2 = float(input ("Introduce otro numero para comprobar si es multiplo :"))
if num1/num2 >5 :
        print("correcto")
elif num2/2>0:
        print("Es par")
else :
        if num1 > 2 and num1 <10:
                print("el numero esta entre el 1 y el 10")
print("FIN")