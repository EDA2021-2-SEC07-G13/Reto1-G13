"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

from io import SEEK_SET
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo, eliga el tipo de lista a usar y su tamaño")
    print("2- Listar cronológicamente los artistas")
    print("3- Listar cronológicamente las adquisiciones")
    print("4- Clasificar las obras de un artista por técnica")
    print("5- Clasificar las obras por la nacionalidad de sus autores")
    print("6- Calcular el transporte de obras de un departamento")
    print("7- Proponer una nueva exposición en el museo")
    print('8')

def initCatalog(list_type):
    """
    Inicializa el catalogo de autores y obras
    """
    return controller.initCatalog(list_type)

def loadData(catalog):
    """
    Carga los libros en la estructura de datos
    """
    controller.loadData(catalog)

def printSortResults(ord_artworks, sample = 10):
    size = lt.size(ord_artworks)
    if size > sample:
        print("Las primeras ", sample, " obras ordenadas cronologicamente son:")
        i=1
        while i <= sample:
            artwork = lt.getElement(ord_artworks,int(i))
            print('Titulo: ' + artwork['Title'] + ' Date Acquired: ' +
                  artwork['DateAcquired'])
            i+=1



"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Eliga y digite el numero dependiendo el tipo de lista a usar")
        print("1- ARRAY LIST")
        print("2- LINKED LIST")
        pick_list = input("Seleccione una opcion para continuar")
        list_type = 'LINKED_LIST'
        if int(pick_list) != 1 and int(pick_list) != 2:
            print("Ejecute de nuevo el programa y eliga una opcion valida")
            break
        elif int(pick_list) == 1:
            list_type = 'ARRAY_LIST'
        
                

        print('----------------')
        print("Cargando información de los archivos ....")
        catalog = initCatalog(list_type)
        loadData(catalog)
        size=str(lt.size(catalog['artists']))
        sizeartists=(lt.size(catalog['artists']))
        sizeartworks=(lt.size(catalog['artworks']))
        artist=catalog['artists']
        artworks=catalog['artworks']
        print('Artistas cargados: ' +str(sizeartists))
        print('Obras cargadas: ' + str(sizeartworks))
        print('Last 3 artists')
        for i in range(0,3):
            print('Artista '+str(sizeartists-2+i)+': '+(lt.getElement(artist,sizeartists-2+i))['DisplayName'])
        print('----------------')
        print('Last 3 artworks')
        for i in range(0,3):
            print('Obra '+str(sizeartworks-2+i)+': '+(lt.getElement(artworks,sizeartworks-2+i))['Title'])
        print('----------------')



    elif int(inputs[0]) == 3:
        size = int(input("Indique tamaño de la muestra (mayor a 10 para que se despliege una muestra de los 10 primeros): "))
        if size > sizeartworks:
            print("Eliga un valor menor a la totalidad de archivos ", str(sizeartworks), " para realizar la operacion")
        else:    
            print("Eliga el tipo de algortimo a usar para el ordenamiento de las obras")
            print("1- Insertion Sort")
            print("2- Shell Sort")
            print("3- Merge Sort")
            print("4- Quick sort")
            algorithm = int(input("Seleccione una opcion para continuar"))
            result = controller.sortArtworks(catalog, int(size), algorithm)
            print("Para la muestra de", size, " elementos, el tiempo (mseg) es: ",str(result[0]))
            printSortResults(result[1])

        
    else:
        sys.exit(0)







