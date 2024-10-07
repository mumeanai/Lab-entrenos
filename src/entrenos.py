import csv
from collections import namedtuple
from datetime import datetime

Entreno = namedtuple('Entreno', 'tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido')

def lee_entrenos(ruta):
    with open(ruta, encoding = 'utf-8') as f: 
        lector = csv.reader(f)
        next(lector)
        
        res = []
       
        for tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido in lector: 
           
            #str de candena, time de tiempo, y p de parse, que significa analizar para extraer informacion
            fechahora = datetime.strptime(fechahora, "%d/%m/%Y %H:%M")
           
            duracion = int(duracion)
            calorias = int(calorias)
            distancia = float(distancia)
            frecuencia = int(frecuencia)
            
            # if compartido == "N":
            #     compartido = False
            # else:
            #     compartido = True
            #este if se puede resumir en una sola línea:
            compartido = compartido == "S"
            
            tupla = Entreno(tipo, fechahora, ubicacion, duracion, calorias, distancia, frecuencia, compartido)
            res.append(tupla)
            
        return res
    
    
def tipos_entreno(entrenos):
    '''
    Recibe una lista de tuplas de tipo Entreno, y devuelve una lista
    con todos los tipos de entrenamientos en orden alfabético y sin
    repetir ninguno.
    
    Como lo hacemos: 
    Creamos un conjunto, recorremos los entrenos, y para cada entreno añadimos al conjunto el tipo de ese entreno
    Devolvemos una lista con los elementos de ese conjunto , ordenanada alfabéticamente.
    '''
    tipos = set()
    for e in entrenos:
        e.tipo.add(e.tipo) #es el equivalente de append (que es para listas), de los conjuntos
    return sorted(tipos) # recibe cualquier coleccion de elementos y devuelve una lista ordenada de estos
    
    
def entrenos_duracion_superior(entrenos, d):
    lista_duracion = []
    for e in entrenos: 
        if e.duracion > d:
            lista_duracion.append(e.duracion)
    return lista_duracion

def suma_calorias(entrenos, f_inicio, f_fin):
    calorias_totales = 0
    for e in entrenos:
        if f_inicio <= e.fecha <= f_fin:
            calorias_totales += e.calorias
    return calorias_totales
