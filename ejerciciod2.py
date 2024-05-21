def Read_colaboradores(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            colaboradores = [linea.strip() for linea in archivo.readlines()]
        return colaboradores
    except FileNotFoundError:
        return []

def Write_colaboradores(nombre_archivo, colaboradores):
    with open(nombre_archivo, 'w') as archivo:
        for colaborador in colaboradores:
            archivo.write(colaborador + '\n')

def See_colaboradores(colaboradores, numero_a_mostrar=5):
    for i, colaborador in enumerate(colaboradores[:numero_a_mostrar]):
        print(f"{i+1}. {colaborador}")

def Join_colaborador(nombre_archivo, colaboradores):
    if len(colaboradores) >= 15:
        print("No se pueden agregar más colaboradores. Se ha alcanzado el límite de 15.")
        return colaboradores
    
    nuevo_colaborador = input("Ingrese el nombre del nuevo colaborador: ").strip().upper()
    colaboradores.append(nuevo_colaborador)
    Write_colaboradores(nombre_archivo, colaboradores)
    return colaboradores

def main():
    nombre_archivo = 'colaboradores.txt'
    colaboradores = Read_colaboradores(nombre_archivo)
    
    if not colaboradores:
        print("El archivo no existe o está vacío. Creando un archivo nuevo.")
        colaboradores = []
        Write_colaboradores(nombre_archivo, colaboradores)
    
    while True:
        print("\nMenú:")
        print("1. Mostrar colaboradores")
        print("2. Agregar colaborador")
        print("3. Salir")
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == '1':
            numero_a_mostrar = input("Ingrese el número de colaboradores a mostrar (presione Enter para mostrar 5): ").strip()
            if numero_a_mostrar.isdigit():
                numero_a_mostrar = int(numero_a_mostrar)
            else:
                numero_a_mostrar = 5
            See_colaboradores(colaboradores, numero_a_mostrar)
        elif opcion == '2':
            colaboradores = Join_colaborador(nombre_archivo, colaboradores)
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
