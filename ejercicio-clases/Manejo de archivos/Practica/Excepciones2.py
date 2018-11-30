#Ejemplo de manejo de excepciones.

try:
	numero1= input("Ingrese un número \n")
	numero1= int(numero1)
	numero2= input("Ingrese el numero 2 \n")
	numero2 = int(numero2)
	operacion = numero1/numero2
	print("El valor de la operacion es %d"%(operacion))
	edad = input("Edad del estudiante \n")
	edad = int(edad)
	print("Su edad es: %d"%(edad))
except NameError as e:
	print("Ingrese una valor valida:%s"%(e))
except ValueError as e:
	print("Existe un error (%s) : %s"%(e.__class__,e))
except ZeroDivisionError as e:
	print("Existe un error (%s) : %s"%(e.__class__,e))
#except Exception as e:
#	print("Existe un error (%s): %s"%(e.__class__,e))