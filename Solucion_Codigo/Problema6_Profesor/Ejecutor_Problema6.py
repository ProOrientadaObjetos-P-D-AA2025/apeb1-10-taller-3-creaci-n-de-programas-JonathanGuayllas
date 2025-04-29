from Problema_6 import Profesor

def main():
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    sueldo_basico = float(input("Ingrese el sueldo básico: "))
    cedula = input("Ingrese la cédula: ")
    # Objeto
    profesor = Profesor(nombre, apellido, sueldo_basico, cedula)
    # llamo al metodo
    profesor.calcular_sueldo_total()
    
    # Datos Pantalla
    print("\n---- Datos del Profesor ----\n")
    print(profesor)
    print("-" * 32)

if __name__ == "__main__":
    main()