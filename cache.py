__author__ = 'Cristina Barreno'

import sys

#Guardar Parametro recibidos por consola
if len(sys.argv) != 4:
    print "La cantidad de argumentos ingresada no es correcta"
file = sys.argv[1]
action = sys.argv[2]
cachesize = sys.argv[3]

#Lectura de archivo y se guarda en una lista
archi=open(file,'r')
listamd=archi.readlines()
archi.close()

#Creación de cache tam de cachesize
cache=list(cachesize)
