#clade de objeto
class Pedido:
    #contructor
    def __init__(self, numero, fecha, libro):
        #atributos
        self.numero = numero
        self.fecha = fecha
        self.libro = libro
#mutadores
    def set_nomero (self, nuevo_numero):
        self.nuevo_numero = nuevo_numero
        
    def set_fecha (self, nuevo_fecha):
        self.nuevo_fecha = nuevo_fecha

    def set_libro (self, nuevo_libro):
        self.nuevo_libro = nuevo_libro
#accesadores
    def get_numero(self):
        return self.numero
    
    def get_fecha(self):
        return self.fecha
    
    def get_libro(self):
        return self.libro