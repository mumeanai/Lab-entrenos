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
    
def test_entrenos_duracion_superior(datos):
    print("Probando la funcion entrenos_duracion_superior")
    d = 20
    print("Los entrenos con una duración mayor a", d, "son:")
    duracion_superior = entrenos_duracion_superior(datos, d)
    print(duracion_superior)
    
def test_suma_calorias(datos):
    print("Probando la funcion suma_calorias")
    #fecha_inicio = datetime.strptime(input("Introduzca la fecha de inicio:"))
    #fecha_fin = float(input("Introduzca la fecha de fin:"))
    fecha_inicio = 23/11/2019
    fecha_fin = 2/9/2021
    print("La suma de las calorías quemadas en todos los entrenamientos realizados entre las dos fechas son:")
    calorias = suma_calorias(datos, fecha_inicio, fecha_fin)
    
    

if __name__ == "__main__":
    test_lee_entrenos("data/entrenos.csv")
    datos = lee_entrenos("data/entrenos.csv")
    test_tipos_entreno(datos)
    
    test_entrenos_duracion_superior(datos)
    test_suma_calorias(datos)
    