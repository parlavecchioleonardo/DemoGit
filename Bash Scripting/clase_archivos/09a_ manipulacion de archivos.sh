#!/bin/bash
#Author: Leonardo Parlavecchio
#Manipular Archivos

input_type=""
input_name=""
input_text=""
read -p "Desea generar un directorio(1) o un archivo(2) " input_type
if (( $input_type == 1 )) then
    read -p "ingrese el nombre del Directorio: " input_name
    mkdir -m 777 $input_name 
fi

if (( $input_type == 2 )) then
    read -p "Ingrese un nombre para el Archivo: " input_name
    touch $input_name
    read -p "Ingrese un texto para el archivo $input_name: " input_text
    echo $input_text >> $input_name
    echo "Contenido del archivo"
    batcat $input_name
fi
