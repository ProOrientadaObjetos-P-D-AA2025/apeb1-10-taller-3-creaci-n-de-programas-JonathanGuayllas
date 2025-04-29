from Problema_8 import Cheque
import random

def main():
    nombre_cliente = f"{random.randint(1, 100)}"
    nombre_banco = f"{random.randint(1, 50)}"
    valor = random.uniform(0.0, 10000.0)
    
    # Objeto 
    cheque = Cheque(nombre_cliente, nombre_banco, valor)
    # Llamo al metodo
    cheque.calcular_comision()
    
    # Datos en Pantalla
    print("\n---- Datos del Cheque ----\n")
    print(cheque)
    print("-" * 32)

if __name__ == "__main__":
    main()