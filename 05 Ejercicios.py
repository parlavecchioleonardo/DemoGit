#EJERCICIO 01


#PRIMERA FORMA
print('EJERCICIO #1')
print('Escriba "continuar" por favor')
continuar=input()
if continuar != "continuar":
    print("Texto erroneo, saliando del programa")
    quit()


numero1=int(input('Por favor, introduzca el "Primer Numero": '))
numero2=int(input('Por favor, introduzca el "Segundo Numero": '))


if numero1==numero2:
    print(f'Tanto el "Primer Numero": {numero1} como el "Segundo Numero": {numero2} son iguales')  
elif numero1>numero2:
    print(f'El "Primer Numero": {numero1} es mayor al "Segundo Numero": {numero2}')
else:
    print(f'El "Segundo Numero": {numero2} es mayor al "Primer Numero": {numero1}')

#SEGUNDA FORMA
# numero1 = int(input('Por favor, introduzca el "Primer Numero": '))
# numero2 = int(input('Por favor, introduzca el "Segundo Numero": '))

# if numero1 < numero2:
#     print('El "Segundo Numero": {} es mayor al "Primer Numero": {}'.format(numero2, numero1))
# else:
#     print('El "Primer Numero": {} es mayor al "Segundo Numero": {}'.format(numero1, numero2))




#EJERCICIO 02
print("")
print("")
print("")
print('EJERCICIO #2')
print('Escriba "continuar" por favor')
print("")
continuar=input()
if continuar != "continuar":
    print("Texto erroneo, saliando del programa")
    quit()

nombre=input('Por favor, introduzca el Nombre: ')
direccion=input('Por favor, introduzca la Dirección: ')
telefono=input('Por favor, introduzca la Teléfono: ')

persona = {"nombre": nombre, "direccion": direccion, "telefono": telefono}

print("Estos son sus datos introducidos")
print("")
print(f"Nombre: {persona['nombre']}")
print(f"Dirección: {persona['direccion']}")
print(f"Teléfono: {persona['telefono']}")






#EJRCICIO 03
print("")
print("")
print("")
print('EJERCICIO #3')
print('Escriba "continuar" por favor')
print("")
continuar=input()
if continuar != "continuar":
    print("Texto erroneo, saliando del programa")
    quit()

numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
numero3 = float(input("Introduce el tercer número: "))

media = (numero1 + numero2 + numero3) / 3

print(f"La media aritmética de los números introducidos es: {media}")