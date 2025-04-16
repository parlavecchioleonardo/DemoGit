#Ejercicio 01
#Crea un programa que muestre los números impares del 1 al 100, los números deberán aparecer una al lado del otro sin salto de linea.


# numero=[int(input("Por favor introduzca el primer numero: ")),
#         int(input("Por favor introduzca el segundo numero: ")),
#         int(input("Por favor introduzca el tercer numero: ")),
#         int(input("Por favor introduzca un numero: "))]

numeros = [i for i in range(1, 101)]

#Esta es otra manera
#numeros = list(range(1, 101)) 

for i in numeros:
    numero1=i
    resto=numero1%2
    if resto!=0:
        print(f"{i}", end=" ")
