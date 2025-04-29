from Problema_7 import Automotor

def main():
    cedula = input("Ingrese la cédula del dueño: ")
    marca = input("Ingrese la marca del vehículo: ")
    fabricacion = int(input("Ingrese el año de fabricación: "))
    valor = float(input("Ingrese el valor del vehículo: "))
    
    # Objeto
    auto = Automotor(cedula, marca, fabricacion, valor)
    # Metodo llamado
    auto.calcular_valor_matricula()
    
    # Datos Pantalla
    print("\n---- Datos del Vehículo ----\n")
    print(auto)
    print("-" * 32)

if __name__ == "__main__":
    main()