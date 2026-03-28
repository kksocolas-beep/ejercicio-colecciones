# ==============================
# COLECCIONES DE DATOS
# ==============================

estudiantes = []
frutas = set()
notas = {}

def agregar_estudiante():
    nombre = input("Ingrese nombre del estudiante: ")
    estudiantes.append(nombre)
    print("Estudiante agregado.\n")

def mostrar_estudiantes():
    print("\nLista de estudiantes:")
    for e in estudiantes:
        print("-", e)

def agregar_fruta():
    fruta = input("Ingrese una fruta: ")
    frutas.add(fruta)
    print("Fruta agregada.\n")

def mostrar_frutas():
    print("\nFrutas registradas:")
    for f in frutas:
        print("-", f)

def agregar_nota():
    nombre = input("Nombre del estudiante: ")
    nota = float(input("Ingrese la nota: "))
    notas[nombre] = nota
    print("Nota guardada.\n")

def mostrar_notas():
    print("\nNotas de estudiantes:")
    for nombre, nota in notas.items():
        print(nombre, ":", nota)

def buscar_estudiante():
    nombre = input("Ingrese nombre a buscar: ")
    if nombre in estudiantes:
        print("El estudiante sí está en la lista.")
    else:
        print("No encontrado.")

def eliminar_estudiante():
    nombre = input("Ingrese nombre a eliminar: ")
    if nombre in estudiantes:
        estudiantes.remove(nombre)
        print("Eliminado.")
    else:
        print("No existe.")

while True:
    print("\n===== MENÚ =====")
    print("1. Agregar estudiante")
    print("2. Mostrar estudiantes")
    print("3. Agregar fruta")
    print("4. Mostrar frutas")
    print("5. Agregar nota")
    print("6. Mostrar notas")
    print("7. Buscar estudiante")
    print("8. Eliminar estudiante")
    print("9. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_estudiante()
    elif opcion == "2":
        mostrar_estudiantes()
    elif opcion == "3":
        agregar_fruta()
    elif opcion == "4":
        mostrar_frutas()
    elif opcion == "5":
        agregar_nota()
    elif opcion == "6":
        mostrar_notas()
    elif opcion == "7":
        buscar_estudiante()
    elif opcion == "8":
        eliminar_estudiante()
    elif opcion == "9":
        print("Programa finalizado.")
        break
    else:
        print("Opción inválida.")
