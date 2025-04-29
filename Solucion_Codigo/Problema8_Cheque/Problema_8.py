class Cheque:
    # Constructor
    def __init__(self, nombre_cliente, nombre_banco, valor):
        self.nombre_cliente = nombre_cliente
        self.nombre_banco = nombre_banco
        self.valor = valor
        self.comision = 0.0
        
    # Funcion
    def calcular_comision(self):
        self.comision = self.valor * 0.003
        
    # to String
    def __str__(self):
        return (f"Cliente: {self.nombre_cliente}\n"
                f"Banco: {self.nombre_banco}\n"
                f"Valor del Cheque: ${self.valor:.2f}\n"
                f"Comisión: ${self.comision:.2f}")