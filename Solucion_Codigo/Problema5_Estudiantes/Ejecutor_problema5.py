from Problema_5 import Estudiante
import random


def main():
    # dato por teclado
    n = int(input("Ingrese el número de estudiantes: "))
    
    # ciclo for para agregar los estudiantes deseados
    for i in range(n):
        nombre = f"Estudiante: {i+1}"
 
        # Notas aleatorias entre 0 y 10 redondeando a 2 los decimales
        m1 = round(random.uniform(0, 10), 2)
        m2 = round(random.uniform(0, 10), 2)
        m3 = round(random.uniform(0, 10), 2)
        
        # Creo el objeto
        estudiante = Estudiante(nombre, m1, m2, m3)
        
        # Metodos
        estudiante.calcular_promedio()
        estudiante.determinar_estado()
        
        # Datos pantalla
        print("\n---- Estudiantes ----")
        print(estudiante)
        print("-" * 32)

if __name__ == "__main__":
    main()