#Ejemplo de manejo de excepciones.

try:
	edad = input("Edad del estudiante \n")
	edad = int(edad)
	print("Su edad es: %d"%(edad))
except NameError as e:
	print("Ingrese una edad valida:%s"%(e))
except ValueError as e:
	print("Existe un error (%s) : %s"%(e.__class__,e))
except Exception as e:
	print("Existe un error (%s): %s"%(e.__class__,e))