mensaje='Hola mundo'

print(mensaje)

a=0

for i in range(5):
    a+=1
    print(a)

miLista1=["Maria", "Pepe", "Marta", "Antonio"]
miLista2=["Leo", "Estefi", "Mamá", "Snake"]
miLista3=miLista1+miLista2

print(miLista3)

otro_diccionario = dict([("nombre", "Carlos"), ("profesion", "Ingeniero")])
print(otro_diccionario)

tercer_diccionario = dict(nombre="Sofía", pais="Argentina")
print(tercer_diccionario)


print("Programa de evaluacion de notas de Alumnos")

nota_alumno:input() # type: ignore
numero_int = int(nota_alumno)

def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="suspenso"
    return valoracion

print(evaluacion(numero_int))