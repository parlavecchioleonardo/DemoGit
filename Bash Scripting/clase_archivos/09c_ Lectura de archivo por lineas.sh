#!/bin/bash
#Author: Leonardo Parlavecchio
#Lectura de archivos

input_name=$1
echo "========== LECTURA DE ARCHIVOS =========="
cat $input_name
echo "========== Lectura de archivo LINEA POR LINEA =========="
echo "IFS (INTERNAL FIELD SEPARATOR), para leer linea por linea"
while IFS= read line
do
    echo "$line"
done < $input_name


echo "========== Otro Ejemplo de IFS para mostrar que efectivamente se lee linea por linea =========="
echo "IFS (INTERNAL FIELD SEPARATOR), para leer linea por linea"
while IFS= read line
do
    echo "== $line =="
done < $input_name

