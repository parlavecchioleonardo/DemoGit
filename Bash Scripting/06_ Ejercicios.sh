#!/bin/bash
# Author: Leonardo Parlavecchio
# Sentencia Case

opcion=""
read -p "Ingrese una Opción [A-B]: " opcion

if [ "$opcion" == "A" ]; then
    echo "Entré al condicional"
fi
