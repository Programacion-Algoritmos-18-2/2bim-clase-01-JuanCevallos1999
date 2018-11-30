from paquete_archivos.miarchivo import * #Importamos las clases
from paquete_modelo.mimodelo import * #Importamos la clase

m = MiArchivo() # objeto para leer el archivo
m2 = MiArchivoEscribir() # objeto para escribir el archivo

lista = m.obtener_informacion()
lista = [l.split("|") for l in lista] #Creamos el "arreglo" mediante un split de la lista que creamos

lista = lista[1:] #Empzamos desde el primer valor ya que la posicion 0 no nos sirve
for d in lista:  #For que recorrera cada linea 
    p = Persona(d[0],d[1],d[2],d[3]) #Enviamos los atributos a nuestro objeto
    print(p)
    m2.agregar_informacion(p) #Agregamos lo enviado a nuestro archivo
#Cerramos los archivos
m.cerrar_archivo()
m2.cerrar_archivo()