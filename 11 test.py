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