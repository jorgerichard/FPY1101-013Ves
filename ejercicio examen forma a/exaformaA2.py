import csv
import datetime


ahora = datetime.datetime.now()
# Datos de entradas 
entradas = ["platinum", "gold", "silver"]
precios = {"platinum": 120000, "gold": 80000, "silver": 50000}
asientos_totales = 100
filas = 10 
columnas = 10 
asientos = [["" for _ in range(columnas)] for _ in range(filas)]  # Crear una matriz de asientos vacíos

ubicaciones_compradas = []

ubicaciones_disponibles = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35, 36, 37, 38, 39, 40],
    [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
    [51, 52, 53, 54, 55, 56, 57, 58, 59, 60],
    [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
    [71, 72, 73, 74, 75, 76, 77, 78, 79, 80],
    [81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
    [91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
]

def  comprar_entradas():
    while True:
        try:
            cantidad = int(input("Ingrese cantidad de entradas (1-3): "))
            if cantidad < 1 or cantidad > 3:
                print("Cantidad de entradas no válida.")
                continue

            mostrar_ubicaciones()
            for i in range(cantidad):
                while True:
                    asiento = int(input(f"Seleccione el número de asiento para la entrada {i+1}: "))
                    if asiento < 1 or asiento > asientos_totales:
                        print("Número de asiento debe ser entre 1 y 100.")
                    else:
                        fila = (asiento - 1) // columnas
                        columna = (asiento - 1) % columnas
                        if asientos[fila][columna] != "":
                            print("El asiento no está disponible.")
                        else:
                            run = input("Ingrese el RUN sin puntos ni guion: ").strip()
                            asientos[fila][columna] = run
                            print("Asiento registrado correctamente.")
                            break
            print("Operación realizada correctamente.")
            break
        except ValueError:
            print("Valor ingresado no es válido.")

def mostrar_ubicaciones():
    print("\nUbicaciones:")
    for i in range(filas):
        for j in range(columnas):
            estado = "X" if asientos[i][j] != "" else "O"
            print(f"{i * columnas + j + 1:02d} [{estado}] ", end="")
        print()  # Salto de línea después de cada fila

def ver_listado():
    asistentes = sorted([run for fila in asientos for run in fila if run != ""])
    print("\nListado de asistentes (por RUN):")
    for run in asistentes:
        print(run)

def mostrar_ganancias():
    total_ganancias = 0
    cantidades = {"platinum": 0, "gold": 0, "silver": 0}

    for i in range(filas):
        for j in range(columnas):
            if asientos[i][j] != "":
                asiento_num = i * columnas + j + 1
                if asiento_num <= 20:
                    tipo = "platinum"
                elif asiento_num <= 50:
                    tipo = "gold"
                else:
                    tipo = "silver"

                cantidades[tipo] += 1 
                total_ganancias += precios[tipo]

    print("\nGanancias Totales:")
    for tipo in entradas:
        cantidad = cantidades[tipo]
        total = cantidad * precios[tipo]
        print(f"{tipo:<10}\t${precios[tipo]:>8,}\t{cantidad:>3}\t${total:>10,}")
    print(f"TOTAL\t\t\t{sum(cantidades.values()):>3}\t${total_ganancias:>10,}")

def menu():
    while True:
        try:
            print("*** Menú ***")
            print("1. Comprar entradas")
            print("2. Mostrar ubicaciones disponibles")
            print("3. Ver listado de asistentes")
            print("4. Mostrar ganancias totales")
            print("5. Salir...")
            op = int(input("Seleccione una opción: "))

            if op == 1:
                comprar_entradas()
            elif op == 2:
                mostrar_ubicaciones()
            elif op == 3:
                ver_listado()
            elif op == 4:
                mostrar_ganancias()
            elif op == 5:
                print("El programa está saliendo...\n desarrollado por jorgerichard")  
                print("Fecha y hora actual:", ahora.strftime("%Y-%m-%d %H:%M:%S"))       
                break
        except ValueError:
            print("Opción no válida.")

menu()
