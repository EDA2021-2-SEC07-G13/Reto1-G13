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
import os
import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from datetime import *


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

def printSortResultsArtworks(ord_artworks, fecha_1, fecha_2):
    
    size = lt.size(ord_artworks)
    
    total_purchase = 0
    pos_1 = 1
    pos_2 = 1

    yf1, mf1, df1 = list(str(fecha_1).split("-"))
    yf2, mf2, df2 = list(str(fecha_2).split("-"))
    fecha_1_date = date(int(yf1) , int(mf1), int(df1))
    fecha_2_date = date(int(yf2) , int(mf2), int(df2))
    

    for x in range(1,size+1):
        
        if len(list(str((lt.getElement(ord_artworks,pos_1+1))['DateAcquired']).split("-"))) != 3 :
            break
        yx , mx, dx = list(str((lt.getElement(ord_artworks,x))['DateAcquired']).split("-"))
        date_artwork_fecha = date(int(yx) , int(mx), int(dx))

        if (lt.getElement(ord_artworks,x))['DateAcquired'] == fecha_1_date:
            print("======")
            
            break
        elif date_artwork_fecha < fecha_1_date:
            pos_1 += 1
        elif  date_artwork_fecha > fecha_1_date:
            
            break   
        

    pos_2 = 1

    for w in range(1,size+1):

        if len(list(str((lt.getElement(ord_artworks,pos_2+1))['DateAcquired']).split("-"))) != 3:
            break

        yw , mw, dw = list(str((lt.getElement(ord_artworks,w))['DateAcquired']).split("-"))
        date_artwork_fecha = date(int(yw) , int(mw), int(dw))

        if (lt.getElement(ord_artworks,w))['DateAcquired'] == fecha_2_date:
            print("======")
            if (lt.getElement(ord_artworks,w+1))['DateAcquired'] != fecha_2_date:
                print("este?")
                break
            else: 
                pos_2 += 1 
        elif date_artwork_fecha < fecha_2_date:
             pos_2 += 1
        elif date_artwork_fecha > fecha_2_date:
            pos_2 -= 1
            break               
        
    for p in range(pos_1, pos_2+1):
        if str((lt.getElement(ord_artworks,p))['CreditLine']) == 'Purchase':
            total_purchase += 1    



    print("El total de obras para este rango fue de ", str(size - pos_1 - 1 - (size - pos_2) ), "obras")
    print("Las primeras 3 y ultimas 3 obras ordenadas cronologicamente para el rango ", str(fecha_1), " - " , str(fecha_2),  "son:")
    print('El total de obras adquiridas por compra en el rango es de: ', total_purchase)

    
    artwork_1 = lt.getElement(ord_artworks,int(pos_1))
    id_artwork1 = str(artwork_1['ConstituentID']).replace("[","").replace("]","")
    list_id_artwork_1 = id_artwork1.split(",")
    artistas_artwork1 = ""
    
    for x in list_id_artwork_1:
        for y in range(1,lt.size(artist)+1):
            
            if str((lt.getElement(artist,y))['ConstituentID']).replace("[","").replace("]","") == x:
                artistas_artwork1 =  str((lt.getElement(artist,y))['DisplayName'])
                break
    
    print('Titulo: ' + artwork_1['Title'] +' Artista(s): ' + str(artistas_artwork1) +  ' Date Acquired: ' +
    artwork_1['DateAcquired'] + ' Medio: ' + artwork_1['Medium'] + ' Dimensions: ' + artwork_1['Dimensions'])



    artwork_2 = lt.getElement(ord_artworks,int(pos_1+1))
    id_artwork2 = str(artwork_2['ConstituentID']).replace("[","").replace("]","")
    list_id_artwork_2 = id_artwork2.split(",")
    artistas_artwork2 = ""
    
    for x in list_id_artwork_2:
        for y in range(1,lt.size(artist)+1):
            
            if str((lt.getElement(artist,y))['ConstituentID']).replace("[","").replace("]","") == x:
                artistas_artwork2 =  str((lt.getElement(artist,y))['DisplayName'])
                break

    print('Titulo: ' + artwork_2['Title'] +' Artista(s): ' + str(artistas_artwork2) +  ' Date Acquired: ' +
    artwork_2['DateAcquired'] + ' Medio: ' + artwork_2['Medium'] + ' Dimensions: ' + artwork_2['Dimensions'])


            
    artwork_3 = lt.getElement(ord_artworks,int(pos_1+2))
    id_artwork3 = str(artwork_3['ConstituentID']).replace("[","").replace("]","")
    list_id_artwork_3 = id_artwork3.split(",")
    artistas_artwork3 = ""
    
    for x in list_id_artwork_3:
        for y in range(1,lt.size(artist)+1):
            
            if str((lt.getElement(artist,y))['ConstituentID']).replace("[","").replace("]","") == x:
                artistas_artwork3 =  str((lt.getElement(artist,y))['DisplayName'])
                break
    print('Titulo: ' + artwork_3['Title'] +' Artista(s): ' + str(artistas_artwork3) +  ' Date Acquired: ' +
    artwork_3['DateAcquired'] + ' Medio: ' + artwork_3['Medium'] + ' Dimensions: ' + artwork_3['Dimensions'])



    artwork_4 = lt.getElement(ord_artworks,int(pos_2-2))
    id_artwork4 = str(artwork_4['ConstituentID']).replace("[","").replace("]","")
    list_id_artwork_4 = id_artwork4.split(",")
    artistas_artwork4 = ""
    
    for x in list_id_artwork_4:
        for y in range(1,lt.size(artist)+1):
            
            if str((lt.getElement(artist,y))['ConstituentID']).replace("[","").replace("]","") == x:
                artistas_artwork4 =  str((lt.getElement(artist,y))['DisplayName'])
                break
    print('Titulo: ' + artwork_4['Title'] +' Artista(s): ' + str(artistas_artwork4) +  ' Date Acquired: ' +
    artwork_4['DateAcquired'] + ' Medio :' + artwork_4['Medium'] + ' Dimensions: ' + artwork_4['Dimensions'])



    artwork_5 = lt.getElement(ord_artworks,int(pos_2-1))
    id_artwork5 = str(artwork_5['ConstituentID']).replace("[","").replace("]","")
    list_id_artwork_5 = id_artwork5.split(",")
    artistas_artwork5 = ""
    
    for x in list_id_artwork_5:
        for y in range(1,lt.size(artist)+1):
            
            if str((lt.getElement(artist,y))['ConstituentID']).replace("[","").replace("]","") == x:
                artistas_artwork5 =  str((lt.getElement(artist,y))['DisplayName'])
                break
    print('Titulo: ' + artwork_5['Title'] +' Artista(s): ' + str(artistas_artwork5) +  ' Date Acquired: ' +
    artwork_5['DateAcquired'] + ' Medio: ' + artwork_5['Medium'] + ' Dimensions: ' + artwork_5['Dimensions'])


            
    artwork_6 = lt.getElement(ord_artworks,int(pos_2))
    id_artwork6 = str(artwork_6['ConstituentID']).replace("[","").replace("]","")
    list_id_artwork_6 = id_artwork6.split(",")
    artistas_artwork6 = ""
    
    for x in list_id_artwork_6:
        for y in range(1,lt.size(artist)+1):
            
            if str((lt.getElement(artist,y))['ConstituentID']).replace("[","").replace("]","") == x:
                artistas_artwork6 =  str((lt.getElement(artist,y))['DisplayName'])
                break
    print('Titulo: ' + artwork_6['Title'] +' Artista(s): ' + str(artistas_artwork6) +  ' Date Acquired: ' +
    artwork_6['DateAcquired'] + ' Medio: ' + artwork_6['Medium'] + ' Dimensions: ' + artwork_6['Dimensions'])

def printSortResultsArtistArtowrk_Teqc(ord_artworkId,codigo_artista):
    
    size = lt.size(ord_artworkId)
    total_obras = 0
    total_medios = 0
    tipos_medios = lt.newList()
    

    for x in range(1, size+1):
        
        if codigo_artista in str(lt.getElement(ord_artworkId,x)['ConstituentID']).replace("[","").replace("]",""):
            total_obras += 1
            if lt.isPresent(tipos_medios, lt.getElement(ord_artworkId,x)['Medium']) == 0:
                lt.addLast(tipos_medios, ( lt.getElement(ord_artworkId,x)['Medium'], 1))
                total_medios += 1
            else:
                pos = lt.isPresent(tipos_medios, lt.getElement(ord_artworkId,x)['Medium'])
                element = lt.getElement(tipos_medios, pos)
                lt.changeInfo(tipos_medios,pos,(element[1],element[2]+1))    

    print("total obras", str(total_obras))
    print("total medios", str(total_medios))

    num_medio_mas_usado = 0
    medio_mas_usado = ''
    print( 'Medios usados y su cantidad:')
    for x in range(1, lt.size(tipos_medios)+1):
        print( lt.getElement(tipos_medios,x))
        if lt.getElement(tipos_medios,x)[1] > num_medio_mas_usado:
            num_medio_mas_usado = lt.getElement(tipos_medios,x)[1]
            medio_mas_usado = lt.getElement(tipos_medios,x)[0]

    print('El medio mas usado es: ', str(medio_mas_usado))
    print("obras con el medio mas usado")
    for x in range(1, size+1):
        if codigo_artista in str(lt.getElement(ord_artworkId,x)['ConstituentID']).replace("[","").replace("]",""):
            if medio_mas_usado in str(lt.getElement(ord_artworkId,x)['Medium']):
                print('Titulo: ', str(lt.getElement(ord_artworkId,x)['Title']), ' Fecha: ',str(lt.getElement(ord_artworkId,x)['Date']),' Medio: ',str(lt.getElement(ord_artworkId,x)['Medium']),'Dimensiones', str(lt.getElement(ord_artworkId,x)['Dimensions']))


    


            
        


        



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
        fecha_1 = (input("Ingrese la fecha incial desde la cual se tomaran las obras en el formato AAAA-MM-DD: "))
        fecha_2 = (input("Ingrese la fecha final hasta la cual se tomaran las obras en el formato AAAA-MM-DD: "))

        if len(list(fecha_1.split("-"))) != 3 or len(list(fecha_2.split("-"))) != 3:
            print('Ingrese la fecha en el formato valido AAAA-MM-DD')
            
        else:    
            y1, m1, d1 = list(fecha_1.split("-"))
            y2, m2, d2 = list(fecha_2.split("-"))

            valor_fecha_1 = date(int(y1), int(m1), int(d1))
            valor_fecha_2 = date(int(y2), int(m2), int(d2))

            if valor_fecha_1 > valor_fecha_2:
                print("La fecha inicial no puede ser mayor a la final, vuelva a intentarlo")
            else:    
                result = controller.sortArtworks(catalog)
                printSortResultsArtworks(result[1], fecha_1, fecha_2)

    elif int(inputs[0]) == 4:
        artist_name = input("Ingrese el nombre del artista")
        nombres_artistas = lt.newList()
        id_artistas = lt.newList()

        


        for x in range(1,lt.size(artist)):
            lt.addLast(nombres_artistas, lt.getElement(artist,x)['DisplayName'])
            lt.addLast(id_artistas, lt.getElement(artist,x)['ConstituentID'])

        

        if lt.isPresent(nombres_artistas, artist_name) == 0:
            print("Digite un nombre de artista valido")
            1
        else:
            print("esta el artista")
            pos = lt.isPresent(nombres_artistas, artist_name) 
            codigo_artista = lt.getElement(id_artistas,pos)
            result = controller.sortArtistArtworks_tecq(catalog)
            printSortResultsArtistArtowrk_Teqc(result[1],codigo_artista)
        
    else:
        sys.exit(0)







