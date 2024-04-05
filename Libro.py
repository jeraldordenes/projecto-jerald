#clase de objeto
class Libro:
    #contructor
    def __init__(self, titulo, autor, genero, precio, stock):
    #atriburos
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.precio = precio
        self.stock = stock
    #mutadores
    def set_titulo (self, nuevo_titulo):
        self.nuevo_titulo = nuevo_titulo
    
    def set_autor (self, nuevo_autor):
        self.nuevo_autor = nuevo_autor    
    
    def set_genero (self, nuevo_genero):
        self.nuevo_genero = nuevo_genero
    
    def set_precio (self, nuevo_precio):
        self.nuevo_precio = nuevo_precio
    
    def set_stock (self, nuevo_stock):
        self.nuevo_stock = nuevo_stock
    #accesadores
    def get_titulo(self):
        return self.titulo 
    
    def get_autor(self):
        return self.autor 
    
    def get_genero(self):
        return self.genero 
    
    def get_precio(self):
        return self.precio 
    
    def get_stock(self):
        return self.stock 