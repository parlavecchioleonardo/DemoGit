#!/bin/bash
# Author: Leonardo Parlavecchio
# Sentencia Case

opcion=""
read -p "Ingrese una Opción [A-B]: " opcion

if [ "$opcion" == "A" ]; then
    echo "Entré al condicional"
fi

case $opcion in
    "A") echo "Ha ingresado la Opción A";;
    "B") echo "Ha ingresado la Opción B";;
    [C-Z]) echo "Ha ingresado un valor fuera del rango";;
    *) echo "Por favor solo caracteres dentro del rango [A-B]";;
esac
