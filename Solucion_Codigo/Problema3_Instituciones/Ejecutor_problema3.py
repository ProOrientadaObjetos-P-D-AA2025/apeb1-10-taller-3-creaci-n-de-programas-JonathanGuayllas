from Problema_3 import InstitucionesEducativas

def main():
    
    # Ingreso de datos por teclado
    nombre = input("Nombre de la institución: ")
    tipo = input("Tipo de institución: ")
    numeroAlum = int(input("Número de alumnos: "))
    numeroDoc = int(input("Número de docentes: "))
    numeroSed = int(input("Número de sedes: "))
    gastosEst = float(input("Gasto proyectado por estudiante: "))

    # Creo el objeto
    institucion = InstitucionesEducativas(
        nombre, tipo, numeroAlum, numeroDoc, numeroSed, gastosEst
    )

    # Calculo el  presupuesto
    institucion.calcularPresupuesto()

    # Muestro en pantalla
    print("\n---- Información de la Institución ----\n")
    print(institucion)

if __name__ == "__main__":
    main()