print("Programa de becas")

distancia_escuela = int(input("Introduce la distancia a la escuela en km: "))
print(distancia_escuela)

numero_hermanos = int(input("Introduce el Nº de hermanos: "))
print(numero_hermanos)

salario_familiar = (int(input("Introduce el salario anual bruto: ")))
print(salario_familiar)

if distancia_escuela > 40 and numero_hermanos > 2 or salario_familiar <= 20000:
    print("Tienes derecho a Beca")
else:
    print("No tienes derecho a Beca")


    
