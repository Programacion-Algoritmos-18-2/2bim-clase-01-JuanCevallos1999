"""
    creación de clases
"""

class Persona():
 
    def __init__(self, n,n1,n2,n3): #La clase recibe cuatro parametros (Nombre y notas)

        self.nombre = n
        self.nota1 = float(n1)
        self.nota2 = float(n2)
        self.nota3 = float(n3)
        self.promedio = 0  #Promedio es un atributo que sera utilizado en otro metodo
    
    def agregar_nombre(self, n): #Metodos set y get
        self.nombre = n
    
    def obtener_nombre(self):
        return self.nombre

    def agregar_nota1(self, n):
        self.nota1 = float(n)

    def obtener_nota1(self):
        return self.nota1   

    def agregar_nota2(self, n):

        self.nota2 = float(n)

    def obtener_nota2(self):
        return self.nota2

    def agregar_nota3(self, n):
        self.nota3 = float(n)
    
    def obtener_nota3(self):
        return self.nota3
#Creamos el método get promedio que va a sacar el resultado del promedio
    def obtener_promedio(self):
        promedio = (self.nota1+self.nota2+self.nota3)/3
        return promedio
    #Usamos el método __str__ para presentar el nombre y el promedio
    def __str__(self):
        return "%s  %.2f " %(self.nombre, self.obtener_promedio())
