class Estudiante:
    # Constructor
    def __init__(self, nombre, materia1, materia2, materia3):
        self.nombre = nombre
        self.materia1 = materia1
        self.materia2 = materia2
        self.materia3 = materia3
        self.promedio = 0.0
        self.estado = ""
    
    # Metodos
    
    def calcular_promedio(self):
        self.promedio = (self.materia1 + self.materia2 + self.materia3) / 3

    def determinar_estado(self):
        self.estado = "Aprobado" if self.promedio >= 6.5 else "Reprobado"
    
    #to String
    def __str__(self):
        return (f"Nombre: {self.nombre}\n"
                f"Nota 1: {self.materia1:.2f}\n"
                f"Nota 2: {self.materia2:.2f}\n"
                f"Nota 3: {self.materia3:.2f}\n"
                f"Promedio: {self.promedio:.2f}\n"
                f"Estado: {self.estado}")