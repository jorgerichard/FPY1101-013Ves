import datetime

# Datos de las entradas
entradas = ["Platinum", "Gold", "Silver"]
precios = {"Platinum": 120000, "Gold": 80000, "Silver": 50000}
asientos_totales = 100
asientos = [""] * asientos_totales

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Comprar entradas")
    print("2. Mostrar ubicaciones disponibles")
    print("3. Ver listado de asistentes")
    print("4. Mostrar ganancias totales")
    print("5. Salir")
    return int(input("Seleccione una opción: "))

# Función para comprar entradas
def comprar_entradas():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad de entradas a comprar (1 a 3): "))
            if cantidad < 1 or cantidad > 3:
                print("Cantidad no válida. Debe ser entre 1 y 3.")
                continue
            
            mostrar_ubicaciones_disponibles()
            
            for i in range(cantidad):
                while True:
                    asiento = int(input(f"Seleccione el número del asiento para la entrada {i+1}: "))
                    if asiento < 1 or asiento > asientos_totales:
                        print("Número de asiento no válido. Debe ser entre 1 y 100.")
                    elif asientos[asiento - 1] != "":
                        print("El asiento no está disponible.")
                    else:
                        run = input("Ingrese el RUN sin puntos ni guión: ").strip()
                        asientos[asiento - 1] = run
                        print("Asiento registrado correctamente.")
                        break
            print("Operación realizada correctamente.")
            break
        except ValueError:
            print("Valor ingresado no es válido. Intente nuevamente.")

# Función para mostrar ubicaciones disponibles
def mostrar_ubicaciones_disponibles():
    print("\nUbicaciones:")
    for i in range(asientos_totales):
        estado = "X" if asientos[i] != "" else "O"
        print(f"{i+1:02d} [{estado}] ", end="")
        if (i + 1) % 10 == 0:
            print()

# Función para ver listado de asistentes
def ver_listado_asistentes():
    asistentes = sorted([run for run in asientos if run != ""])
    print("\nListado de asistentes (por RUN):")
    for run in asistentes:
        print(run)

# Función para mostrar ganancias totales
def mostrar_ganancias_totales():
    total_ganancias = 0
    cantidades = {"Platinum": 0, "Gold": 0, "Silver": 0}
    
    for i in range(asientos_totales):
        if asientos[i] != "":
            if i < 20:
                tipo = "Platinum"
            elif i < 50:
                tipo = "Gold"
            else:
                tipo = "Silver"
            cantidades[tipo] += 1
            total_ganancias += precios[tipo]
    
    print("\nGanancias Totales:")
    for tipo in entradas:
        cantidad = cantidades[tipo]
        total = cantidad * precios[tipo]
        print(f"{tipo}\t${precios[tipo]:,}\t{cantidad}\t${total:,}")
    print(f"TOTAL\t\t\t{sum(cantidades.values())}\t${total_ganancias:,}")

# Función para salir del sistema
def salir():
    fecha_actual = datetime.datetime.now().strftime("%d-%m-%Y")
    print("Programa finalizado…")
    print("Desarrollado por Valeria Ruminot")
    print(f"Fecha: {fecha_actual}")

# Programa principal
def menu():
    while True:
        try:
            opcion = mostrar_menu()
            if opcion == 1:
                comprar_entradas()
            elif opcion == 2:
                mostrar_ubicaciones_disponibles()
            elif opcion == 3:
                ver_listado_asistentes()
            elif opcion == 4:
                mostrar_ganancias_totales()
            elif opcion == 5:
                salir()
                break
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Opción no válida. Debe ingresar un número.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    menu()
