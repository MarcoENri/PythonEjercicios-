def listaTareas():
    tareas = []

    while True:
        print("\n1. Agregar tarea")
        print("\n2. Eliminar tarea")
        print("\n3. Mostrar tareas")
        print("\n4. Salir")
        
        option = input("Seleccione una opción: ")

        if option == '1':
            tarea = input("Ingrese la tarea: ")
            tareas.append(tarea)
        elif option == '2':
            tarea = input("Ingrese la tarea a eliminar: ")
            if tarea in tareas:
                tareas.remove(tarea)
            else:
                print("Tarea no encontrada")
        elif option == '3':
            print("Listado de tareas:")
            for t in tareas:
                print("-", t)
        elif option == '4':
            break
        else:
            print("Opción no válida")

listaTareas()
