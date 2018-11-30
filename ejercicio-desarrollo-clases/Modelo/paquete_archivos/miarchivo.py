
import codecs

class MiArchivo:

    def __init__(self):
        self.archivo = codecs.open("data/informacion.csv","r") #Abre el archivo (ruta,r =read)

    def obtener_informacion(self): #Lee las lineas del archivo
        return self.archivo.readlines()

    def cerrar_archivo(self): #Cerramos el archivo
        self.archivo.close()


class MiArchivoEscribir: #Creamos la clase que nos va a permitir crear otro archivo
    
    def __init__(self):
        self.archivo = codecs.open("data/archivonuevo.csv","a") #Que vaya a esta direccon y sino existe lo crea y añade lo que agrego al finla del archivo

    def agregar_informacion(self, p): #Recibe un parametro de tipo persona y lo agrega en el archivo que creamos
        self.archivo.write("%s-%.2f\n" % (p.nombre, p.obtener_promedio()))

    def cerrar_archivo(self):#cierra el archivo creado
        self.archivo.close() 
