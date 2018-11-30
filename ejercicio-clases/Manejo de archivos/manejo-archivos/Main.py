from paquete_archivos.miarchivo import *
from paquete_modelo.mimodelo import *

m = MiArchivo() # objeto para leer el archivo
m2 = MiArchivoEscribir() # objeto para escribir el archivo

lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]

# print(lista)

lista = lista[1:]
for d in lista:
    p = Persona(d[1],d[0])
    print(p)
    m2.agregar_informacion(p)

m.cerrar_archivo()
m2.cerrar_archivo()
