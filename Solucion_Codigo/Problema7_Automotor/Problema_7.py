class Automotor:
    # constructor
    def __init__(self, cedula_due, marca, fabricacion, valor):
        self.cedula_due = cedula_due
        self.marca = marca
        self.fabricacion = fabricacion
        self.valor = valor
        self.valor_matricula = 0.0
    
    # Metodo
    def calcular_valor_matricula(self):
        self.valor_matricula = 0.002 * self.valor * (2023 - self.fabricacion)
        
    # to String
    def __str__(self):
        return (f"Cédula Dueño: {self.cedula_due}\n"
                f"Marca: {self.marca}\n"
                f"Año de Fabricación: {self.fabricacion}\n"
                f"Valor Vehículo: ${self.valor:.2f}\n"
                f"Valor Matrícula: ${self.valor_matricula:.2f}")