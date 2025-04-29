from Problema_4 import EquipoCelular

def main():
    # Datos por teclado
    sistemaOper = input("Sistema operativo: ")
    pantallaTam = float(input("Tamaño de pantalla: "))
    costoIni = float(input("Costo inicial: "))
    ivaPorc = float(input("IVA (%): "))
    direccionMac = input("Dirección MAC: ")
    imei = input("IMEI: ")

    # Creo Objeto
    celular = EquipoCelular(sistemaOper, pantallaTam, costoIni, ivaPorc, direccionMac, imei)

    # Llamo los metodos 
    celular.calcularIva()
    celular.calcularCostoFinal()

    # Muestro en pantalla
    print("\n---- Detalles del Equipo Celular ----\n")
    print(celular)

if __name__ == "__main__":
    main()