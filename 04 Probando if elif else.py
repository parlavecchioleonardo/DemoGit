print("Verificación de Acceso")

nota = int(input("Introduce tu edad, por favor: "))

if nota<5:
    print("Insuficiente")
elif nota<6:
    print("Suficiente")
elif nota<7:
    print("Bien")
elif nota<9:
    print("Notable")
else:
    print("Sobresaliente")