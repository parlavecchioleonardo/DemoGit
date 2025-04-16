#Ejemplo 01
for i in ["a","b","c"]:
    print(i)

#Ejemplo 02
#En este caso la variable recorre todo el string
for i in "juan@pildorasinformaticas.es":
    print(i)

#Ejemplo 03
#Corroborar que se esta cargando un email
email=False

for i in "juan@pildorasinformaticas.es":
    if i == "@":
        email=True

#if email==True:
if email: #Con poner solamente email ya evalua que sea True
    print("Email es correcto")
else:   
    print("Email incorrecto")

#Ejemplo 04
#Corroborar que se esta cargando un email
email=False
miEmail=input("Por favor introduzca su dirección de correo: ")

for i in miEmail:
    if i == "@":
        email=True

#if email==True:
if email: #Con poner solamente email ya evalua que sea True
    print("Email es correcto")
else:   
    print("Email incorrecto")

#Ejemplo 05
#Corroborar que se esta cargando un email
contador=0
miEmail=input("Por favor introduzca su dirección de correo: ")

for i in miEmail:
    if (i == "@" or i=="."):
        contador=contador+1

if contador==2: #Con poner solamente email ya evalua que sea True
    print("Email es correcto")
else:   
    print("Email incorrecto")

