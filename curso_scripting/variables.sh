# !/bin/bash
#Author: Leonardo Parlavecchio
# Enseñanza de variables en scripting.

numA=2
numB=2

echo "Operadores Aritméticos entre $numA y $numB"

echo "$numA + $numB = " $((numA + numB))
echo "$numA - $numB = " $((numA - numB))
echo "$numA * $numB = " $((numA * numB))
echo "$numA / $numB = " $((numA / numB))

echo "Operadores Relacionales entre $numA y $numB"

echo "$numA > $numB = " $((numA > numB))
echo "$numA < $numB = " $((numA < numB))
echo "$numA >= $numB = " $((numA >= numB))
echo "$numA <= $numB = " $((numA <= numB))
echo "$numA == $numB = " $((numA == numB))
echo "$numA != $numB = " $((numA != numB))

