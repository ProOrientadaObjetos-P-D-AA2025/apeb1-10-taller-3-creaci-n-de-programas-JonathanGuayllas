# importe para números aleatorios
import random

# Clase terreno
class Terreno:
    def __init__(self):
        self.ancho = 0.0
        self.largo = 0.0
        self.valorMeC = 0.0
        self.area = 0.0
        self.costoT = 0.0

    # Sets
    def setAncho(self):
        self.ancho = round(random.uniform(0.0, 100.0),2)  # valor aleatorio entre 0 y 100 

    def setLargo(self):
        self.largo = round(random.uniform(0.0, 100.0),2)   # valor aleatorio entre 0 y 100 

    def setValorMeC(self):
        self.valorMeC = round(random.uniform(0.0, 1000.0),2)  # valor aleatorio entre 0 y 1000

    # Gets
    def getAncho(self):
        return self.ancho

    def getLargo(self):
        return self.largo

    def getValorMeC(self):
        return self.valorMeC
        
    # Procesos 
    
    def calcularArea(self):
        self.area = self.ancho * self.largo

    def calcularTotal(self):
        self.costoT = self.area * self.valorMeC

    # toString() == __str__ (PHYTHON)
    
    def __str__(self):
        return (f"---- Terreno con datos aleatorios ----\n\n"
                f"Ancho: {self.ancho:.2f} metros\n"
                f"Largo: {self.largo:.2f} metros\n"
                f"Valor del metro cuadrado: {self.valorMeC:.2f}\n\n"
                f"---- Costo y Área del terreno ----\n\n"
                f"Área: {self.area:.2f} metros cuadrados\n"
                f"Costo total del terreno: {self.costoT:.2f}")
