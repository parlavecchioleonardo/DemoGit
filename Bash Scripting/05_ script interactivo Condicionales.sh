#!/bin/bash
# Author: Leonardo Parlavecchio
# Script Interactivo - Condionales

#-eq: Igual a
#-ne: No es igual a
#-gt: Mayor a
#-ge: Mayor o igual a
#-lt: Menor a
#-le: Menor o igual a


name""
age=0
year=0

read -p "Ingresa tu nombre: " name
read -p "Ingresa tu edad: " age
read -p "Ingresa el año actual: " year 

echo "Hola, mi nombre es $name y tengo $age años."

echo "==========================================="

if (($age >= 18)); then
    echo "Eres mayor de edad"
else
    echo "No eres mayor de edad"
fi

echo "==========================================="

if [ $age -ge 18 ] && [ $year -eq 2025 ]; then
    echo "$name, Eres mayor de edad, y este año puedes sufragar"
else
    echo "$name, No se cumplen las condiciones para votar"
fi
