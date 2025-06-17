#!/bin/bash
# Author: Leonardo Parlavecchio
# Enseñanza sobre Arreglos - Iteracion

#Asi se declaran los arreglos
numeros=(1 2 3 4 5 6 7 8)
nombres=(diego julian jenifer rosa miguel)
rangos=({A..Z} {20..30})
echo "===== Imprimir todos los valores ====="

echo "Arreglo de Números ${numeros[*]}"
echo "Arreglo de Nombres ${nombres[*]}"
echo "Arreglo de Rangos ${rangos[*]}"


#Asi se declaran los arreglos
numeros=(1 2 3 4 5 6 7 8)
nombres=('diego bastidas' 'julian bastidas' 'jennifer lopez' 'rosa rincon' miguel)
rangos=({A..Z} {20..30})
echo "===== Imprimir tamaño de los arreglos ====="

echo "Tamaño del arreglo numeros:  ${#numeros[*]}"
echo "Tamaño del arreglo nombres:  ${#nombres[*]}"
echo "Tamaño del arreglo rangos:  ${#rangos[*]}"

echo "===== Imprimir un elemento puntual del arreglo ====="

echo "Elemento numero 3 del arreglo números:  ${numeros[3]}"
echo "Elemento numero 3 del arreglo nombres:  ${nombres[3]}"
echo "Elemento numero 3 del arreglo rangos:  ${rangos[3]}"

echo "===== Manipular Arreglos ====="

#Eliminar un elemento del arreglo
unset numeros[0]
echo "Arreglo de Números ${numeros[*]}"
