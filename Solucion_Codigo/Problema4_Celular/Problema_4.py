class EquipoCelular:
    # Constructor
    def __init__(self, sistemaOper, pantallaTam, costoIni, ivaPorc, direccionMac, imei):
        self.sistemaOper = sistemaOper
        self.pantallaTam = pantallaTam
        self.costoIni = costoIni
        self.ivaPorc = ivaPorc
        self.direccionMac = direccionMac
        self.imei = imei
        self.ivaCosIni = 0.0
        self.costoFin = 0.0
    
    # Metodos
    def calcularIva(self):
        self.ivaCosIni = self.costoIni * self.ivaPorc / 100

    def calcularCostoFinal(self):
        self.costoFin = self.costoIni + self.ivaCosIni

    # toString
    def __str__(self):
        return (f"Sistema Operativo: {self.sistemaOper}\n"
                f"Tamaño Pantalla: {self.pantallaTam}\n"
                f"Dirección MAC: {self.direccionMac}\n"
                f"IMEI: {self.imei}\n"
                f"Costo Inicial: ${self.costoIni:.2f}\n"
                f"IVA (%): {self.ivaPorc}%\n"
                f"IVA Calculado: ${self.ivaCosIni:.2f}\n"
                f"Costo Final: ${self.costoFin:.2f}\n")