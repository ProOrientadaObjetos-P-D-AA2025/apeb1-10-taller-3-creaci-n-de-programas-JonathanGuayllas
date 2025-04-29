class Profesor:
    #Constructor
    def __init__(self, nombre, apellido, sueldo_basico, cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.sueldoBas = sueldo_basico
        self.sueldoTot = 0.0
        self.cedula = cedula
    
    # Metodos
    def calcular_sueldo_total(self):
        self.sueldoTot = self.sueldoBas + (self.sueldoBas * 0.2)
    
    #toString
    def __str__(self):
        return (f"Profesor: {self.nombre} {self.apellido}\n"
                f"Cédula: {self.cedula}\n"
                f"Sueldo Básico: ${self.sueldoBas:.2f}\n"
                f"Sueldo Total:  ${self.sueldoTot:.2f}")