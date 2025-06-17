#!/bin/bash
# Author: Leonardo Parlavecchio
# Enseñanza de variables de Scripting

#Los 3 primeros campos no son necesarios

numA=2
numB=2

echo "===================================="

echo "Operadores Aritméticos entre $numA y $numB"

echo "$numA + $numB = " $((numA + numB))
echo "$numA - $numB = " $((numA - numB))
echo "$numA * $numB = " $((numA * numB))
echo "$numA / $numB = " $((numA / numB))

echo "===================================="

echo "Operadores Relacionales entre $numA y $numB"

echo "$numA > $numB = " $((numA > numB))
echo "$numA < $numB = " $((numA < numB))
echo "$numA >= $numB = " $((numA >= numB))
echo "$numA <= $numB = " $((numA <= numB))
echo "$numA == $numB = " $((numA == numB))
echo "$numA != $numB = " $((numA != numB))

echo "===================================="

echo "Operadores de Asignación entre $numA y $numB"

echo "$numA += $numB = " $((numA += numB))
echo "$numA -= $numB = " $((numA -= numB))
echo "$numA *= $numB = " $((numA *= numB))
echo "$numA /= $numB = " $((numA /= numB))
