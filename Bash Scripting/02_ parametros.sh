# !/bin/bash
# Author: Leonardo Parlavecchio
# Ejemplificacion de variables y parametros dinámicos

pwd #Imprime la salida stdout del comando pwd
ubicacion=pwd 
echo $ubicacion #Imprime el valor de la variable y vemos que pwd fue asignada como texto, mas no como comando

#Para asignarle a la variable un comando, se hace de la siguiente manera
ubicacion=$(pwd)
echo $ubicacion
