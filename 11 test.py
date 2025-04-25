contrasena=input("Por favor introduzca su contraseña: ")
lencontrasena=len(contrasena)
vacio=0

for i in contrasena:
    if (i == " "):
        vacio=vacio+1
   

if lencontrasena>=8 and vacio==0:
    print("Ingreso correcto de contraseña")
else:
    print("Ingreso de contraseña incorrecto, la contraseña debe tener mas de 8 caracteres y ningun espacio vacio")