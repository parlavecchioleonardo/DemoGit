#!/bin/bash
# Author: Leonardo Parlavecchio
# Como pasar parametros o argumentos

nombre=$1
apellido=$2

echo "Mi nombre es: $nombre $apellido"


#Al momento de ejecutar el scrip le pasamos los paramentros, asi:
#./03_\ parametros.sh Leonardo Parlavecchio

#Y la consola imprimira
#Mi nombre es: Leonardo Parlavecchio

#Ahora veamos la cantidad de parametros enviados
echo "La cantidad de parametros enviados es: $#"
echo "La cantidad de parametros enviados por el usuario son: $*"
