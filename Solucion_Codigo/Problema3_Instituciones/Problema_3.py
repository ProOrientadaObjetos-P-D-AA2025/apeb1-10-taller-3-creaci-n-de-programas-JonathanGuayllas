class InstitucionesEducativas:
    
    # constructor
    def __init__(self, nombre, tipo, numeroAlum, numeroDoc, numeroSed, gastosEst):
        self.nombre = nombre
        self.tipo = tipo
        self.numeroAlum = numeroAlum
        self.numeroDoc = numeroDoc
        self.numeroSed = numeroSed
        self.gastosEst = gastosEst
        self.presupuesto = 0  # Se calcula con el metodo

    # metodo para calcular presupuesto
    def calcularPresupuesto(self):
        self.presupuesto = self.numeroAlum * self.gastosEst

    #toString    

    def __str__(self):
        return (f"Nombre: {self.nombre}\n"
                f"Tipo: {self.tipo}\n"
                f"Número de Alumnos: {self.numeroAlum}\n"
                f"Número de Docentes: {self.numeroDoc}\n"
                f"Número de Sedes: {self.numeroSed}\n"
                f"Gasto por Estudiante: ${self.gastosEst:.2f}\n"
                f"Presupuesto Total: ${self.presupuesto:.2f}")