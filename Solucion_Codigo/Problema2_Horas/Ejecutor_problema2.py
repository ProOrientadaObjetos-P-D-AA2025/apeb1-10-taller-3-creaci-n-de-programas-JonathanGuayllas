from Problema_2 import EquivalenciaHora

def main():
    # Obtener horas por teclado
    horas = float(input("Introduce la cantidad de horas: "))
    
    # Creo el objeto 
    equivalencia = EquivalenciaHora(horas)
    
    # muestro datos
    print(equivalencia)

if __name__ == "__main__":
    main()