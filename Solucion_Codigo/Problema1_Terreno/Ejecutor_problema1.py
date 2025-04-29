# importo la clase 
from Problema_1 import Terreno

def main():
    # creo el objeto
    terreno = Terreno()

    # Asigno datos aleatorios
    terreno.setAncho()
    terreno.setLargo()
    terreno.setValorMeC()

    # proceso el area y total
    terreno.calcularArea()
    terreno.calcularTotal()

    # Muestro Datos
    print(terreno)

# Hago que solo se ejecute el main
if __name__ == "__main__":
    main()

