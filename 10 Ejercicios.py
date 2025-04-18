#Ejercicio 01
#Crea un programa que muestre los números impares del 1 al 100, los números deberán aparecer una al lado del otro sin salto de linea.

# numero=[int(input("Por favor introduzca el primer numero: ")),
#         int(input("Por favor introduzca el segundo numero: ")),
#         int(input("Por favor introduzca el tercer numero: ")),
#         int(input("Por favor introduzca un numero: "))]

numeros = list(range(1, 101)) 
#Esta es otra manera
#numeros = [i for i in range(1, 101)]

for i in numeros:
    numero1=i
    resto=numero1%2
    if resto!=0:
        print(f"{i}", end=" ")


#Ejercicio 02
#Crea un programa que pida por teclado introducir una contraseña.
#La contraseña no podrá tener menos de 8 caracteres ni espacios en blanco.
#Si la contraseña es correcta el programa imprime "Contraseña OK".
#En caso contrario imprime "Contraseña erróne"
contrasena=input("Por favor introduzca su contraseña: ")
caracteres=0
campovacio=0

for i in contrasena:
    caracteres=caracteres+1
    if (i == " "):
        campovacio=campovacio+1
   

if caracteres>=8 and campovacio==0:
    print("Ingreso correcto de contraseña")
else:
    print("Ingreso de contraseña incorrecto, la contraseña debe tener mas de 8 caracteres y ningun espacio vacio")



#Ejercicio 03
#Crea un programa que evalúe si una dirección de correo electrónico es 
#válida o no en función de si tiene "@" o ".". Hay que tener en cuenta 
#que la dirección se considera correcta si solo tiene una "@" y si tiene uno o más "."
email=False
miEmail=input("Por favor introduzca su dirección de correo: ")
contadorpunto=0
contadorarroba=0

for i in miEmail:
     
    if (i == "@"):
        contadorarroba=contadorarroba+1
    elif (i== "."):
        contadorpunto=contadorpunto+1
    
    if contadorarroba==1 and contadorpunto>=1:
        email=True

if email: #Con poner solamente email ya evalua que sea True
    print("Email es correcto")
else:   
    print("Email incorrecto")