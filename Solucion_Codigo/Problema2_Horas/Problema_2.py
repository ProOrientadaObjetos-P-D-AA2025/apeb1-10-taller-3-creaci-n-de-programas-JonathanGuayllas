class EquivalenciaHora:
    def __init__(self, horas: float):
        self.horas = horas
        self.minutos = 0.0
        self.segundos = 0.0
        self.dias = 0.0
        self.calcularEquivalencia(horas)  # Llamo al metodo
        
        
    # metodo para calcular 
    def calcularEquivalencia(self, horas: float):
        self.minutos = horas * 60
        self.segundos = self.minutos * 60
        self.dias = horas / 24
    
    # to String
    def __str__(self):
        return (f"---- Equivalencia de {self.horas} horas ----\n\n"
                f"Horas: {self.horas}\n"
                f"Minutos: {self.minutos}\n"
                f"Segundos: {self.segundos}\n"
                f"Días: {self.dias}")