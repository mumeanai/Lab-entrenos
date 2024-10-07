from entrenos import *

def test_lee_entrenos(ruta):
    print("Probando la funcion lee_entrenos: ")
    datos = lee_entrenos("data/entrenos.csv")
    print("Leídos:", len(datos), "registros.")
    print("Primer elemento:", datos[0])
    print("Segundo elemento:", datos[1])
    print("Tercer elemento:", datos[2])
    
def test_tipos_entreno(datos):
    print("Probando la funcion tipos_entreno")
    tipos = tipos_entreno(datos)
    print("Los distintos tipos de entreno son:")
    print(tipos)
    


if __name__ == "__main__":
    test_lee_entrenos("data/entrenos.csv")
    datos = lee_entrenos("data/entrenos.csv")
    test_tipos_entreno(datos)