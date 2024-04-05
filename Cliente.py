#clase de objeto
class Cliente:
    #constructor   
    def __init__(self, nombre, direccion, correo):
        #atributos
        self.nombre = nombre
        self.direccion = direccion
        self.correo = correo
    
    #mutadores
    def set_nombre (self, nuevo_nombre):
        self.nuevo_nombre = nuevo_nombre
    
    def set_direccion (self, nuevo_direccion):
        self.nuevo_direccion = nuevo_direccion
    
    def set_correo (self, nuevo_correo):
        self.nuevo_correo = nuevo_correo
    #accesadores
    def get_nombre(self):
        return self.nombre
    
    def get_direccion(self):
        return self.direccion
    
    def get_correo(self):
        return self.correo