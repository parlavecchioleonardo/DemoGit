print("Programa de evaluacion de notas de Alumnos")

nota_alumno = input("Introduce la nota del alumno: ")
#numero_int = int(nota_alumno)

def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="suspenso"
    return valoracion

print(evaluacion(int(nota_alumno)))