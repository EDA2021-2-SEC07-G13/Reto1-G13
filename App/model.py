"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from DISClib.DataStructures.arraylist import compareElements, defaultfunction
import config as cf
from datetime import *
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import shellsort as ss
from DISClib.Algorithms.Sorting import mergesort as ms
from DISClib.Algorithms.Sorting import quicksort as qs
from DISClib.Algorithms.Sorting import selectionsort as sso

assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog(list_type):
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    catalog = {'artists': None,
               'artworks': None}

    catalog['artists'] = lt.newList(list_type)
    catalog['artworks'] = lt.newList(list_type)
    

    return catalog

# Funciones para agregar informacion al catalogo

def addArtist(catalog, artist):
    # Se adiciona el artista a la lista de artistas
    lt.addLast(catalog['artists'], artist)
    


def addArtwork(catalog, artwork):
    """
    Adiciona un autor a lista de autores, la cual guarda referencias
    a los libros de dicho autor
    """
    lt.addLast(catalog['artworks'], artwork)

  




# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

def cmpArtworkByDateAcquired(artwork1, artwork2):
    """
    Devuelve verdadero (True) si el 'DateAcquired' de artwork1 es menores que el de artwork2
    Args:
    artwork1: informacion de la primera obra que incluye su valor 'DateAcquired'
    artwork2: informacion de la segunda obra que incluye su valor 'DateAcquired'
    """
    

    if len(list(artwork1['DateAcquired'].split("-"))) != 3 and len(list(artwork2['DateAcquired'].split("-"))) == 3:
        return True    
    elif len(list(artwork1['DateAcquired'].split("-"))) == 3 and len(list(artwork2['DateAcquired'].split("-"))) != 3:
        return False
    elif len(list(artwork1['DateAcquired'].split("-"))) != 3 and len(list(artwork2['DateAcquired'].split("-"))) != 3:
        return True
    else: 
        d1, m1, y1 = list(artwork1['DateAcquired'].split("-"))
        d2, m2, y2 = list(artwork2['DateAcquired'].split("-"))

        value = date(int(d1), int(m1), int(y1)) < date(int(d2), int(m2), int(y2))
        return value      




    



# Funciones de ordenamiento

def sortArtworks(catalog, size, algorithm):
    sub_list = lt.subList(catalog['artworks'], 1, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    sorted_list = ""
    if algorithm == 1:
        sorted_list = ins.sort(sub_list, cmpArtworkByDateAcquired)
    elif algorithm == 2:
        sorted_list = ss.sort(sub_list, cmpArtworkByDateAcquired)
    elif algorithm == 3:
        sorted_list = ms.sort(sub_list, cmpArtworkByDateAcquired)   
    elif algorithm == 4:
        sorted_list = qs.sort(sub_list, cmpArtworkByDateAcquired)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list



def busquedad_binaria_begindate(lst,date)->int:
    """Busqueda binaria de un elemento en una lista ordenada ascendentemente,
     devuelve la posición donde se encuentra el elemento,si no está el elemento
     devuelve -1,si hay mas de un elemento devuelve la ultima posición donde está ese elemento; orden de complejidad O(log(n)) """
    i=0
    f=lt.size(lst)
    pos=-1
    encontro=False
    while i<=f and not encontro:
        m=(i+f)//2
        if int(lt.getElement(lst,m)['BeginDate'])==date:
            encontro=True
            pos=m    
        elif date<int(lt.getElement(lst,m)['BeginDate']):
            f=m-1
        else:
            i=m+1
    return pos

def cmpfuntion1(artist1,artist2):
    begindate1=artist1['BeginDate']
    begindate2=artist2['BeginDate']
    begindate1=int(begindate1)
    begindate2=int(begindate2)

    if begindate2>begindate1:
        return True
    else:
        return False




def listarcronologicamente(catalog,ano_inicial,ano_final):
    artists=catalog['artists']
    ms.sort(artists,cmpfuntion1)
    for indice in range(1,lt.size(artists)+1):
        if int(lt.getElement(artists,indice)['BeginDate'])==ano_final and int(lt.getElement(artists,indice+1)['BeginDate'])>ano_final:
            indice_final=indice
        if int(lt.getElement(artists,indice)['BeginDate'])==ano_inicial and int(lt.getElement(artists,indice-1)['BeginDate'])<ano_inicial:
            indice_inicial=indice
    sizesublist=indice_final-indice_inicial
    listadeseada=lt.subList(artists,indice_inicial,sizesublist)

        
   
    return listadeseada

def cmpfuntion2(id1, id2):
    id1=int(id1)
    id2=int(id2)
    if id2 > id1:
        return True
    else:
        return False


def busquedad_binaria_id(lst,id)->int:
    """Busqueda binaria de un elemento en una lista ordenada ascendentemente,
     devuelve la posición donde se encuentra el elemento,si no está el elemento
     devuelve -1,si hay mas de un elemento devuelve la ultima posición donde está ese elemento; orden de complejidad O(log(n)) """
    i=0
    f=lt.size(lst)
    pos=-1
    encontro=False
    while i<=f and not encontro:
        m=(i+f)//2
        if (int(lt.getElement(lst,m))==int(id)):
            encontro=True
            pos=m    
        elif int(id)<int(lt.getElement(lst,m)):
            f=m-1
        else:
            i=m+1
    return pos

def cmpfuntion3(inf1,inf2):
    frec1=inf1[1]
    frec2=inf2[1]
    if frec2<frec1:
        return True
    else:
        return False
def cmpfuntion4(id1,id2):
    id1=id1[0]
    id2=id2[0]
    if int(id2)>int(id1):
        return True



def nacionalidadautores(catalog):
    artists=catalog['artists']
    idslist=lt.newList('ARRAY_LIST')
    artworks=catalog['artworks']
    dicnat={}
    for indice in range(1,lt.size(artists)+1):
        artist=lt.getElement(artists,indice)
        nati=artist['Nationality'].lower()
        if nati=='' or nati=='nationality unknown':
            nati='unknow'
        dicnat[nati]=0
        
    for indice in range(1,lt.size(artworks)+1):
        artwork=lt.getElement(artworks,indice)
        ids=artwork.pop('ConstituentID')
        ids=ids.replace(']','').replace('[','').split(',')
        for id in ids:
            lt.addLast(idslist,id)

    for indice in range(1,lt.size(artists)+1):
        artist=lt.getElement(artists,indice)
        if artist=='':
            artist='artist unknow'
        idartis=int(artist['ConstituentID'])
        nation=artist['Nationality'].lower()
        if nation=='' or nation=='nationality unknown':
            nation='unknow'
        for indice2 in range(1,lt.size(idslist)+1):
            if int(lt.getElement(idslist,indice2))==idartis:
                dicnat[nation]+=1
          
    finallist=lt.newList('ARRAY_LIST')
    for key in dicnat:
        lt.addLast(finallist,(key,dicnat[key]))
    ms.sort(finallist,cmpfuntion3)
    
    


            


    return finallist



    



            


            

