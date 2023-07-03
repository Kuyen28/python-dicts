# Con listas y diccionarios podemos representar estructuras completas similares a los
# que encontramos en el mundo real. Por ejemplo, podríamos tener un listado de estudiantes.
# Cada estudiantes tiene nombre, apellido, curos y una lista de sus calificaciones.
# Ejemplo

students = [
    {
        "name": "Vanessa",
        "lastname": "Monsó",
        "course": "Programación B",
        "grades": [100,90,95,100],
        "active": False
    },
    {"name": "Zack",
        "lastname": "Galaz",
        "course": "Mecánica automotriz",
        "grades": [90,100,85,100],
        "active": True
}
]

# Ejercicio. Manipular el arreglo de estudiantes para que muestre la siguiente informacion por cada uno.
# Estudiante: Nombre Apellido
# Curso: Nombre del curso
# Promedio de notas: x
# Estado: Activo/Inactivo

for student in students:
    print("Estudiante:", student["name"], student["lastname"])
    print("Curso:", student["course"])

    sum = 0
    grades = student["grades"]
    for grade in grades:
        sum += grade

    print("Promedio de notas:", sum/len(grades))

    if student["active"]:
        print("Estado: Activo")
    else:
        print("Estados: Inactivo")
