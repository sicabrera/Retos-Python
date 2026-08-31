import os 

def ventasMinisuper():
    ##Tu misión: Registra las ventas de lunes a domingo. Calcula el total semanal y el promedio diario.
    os.system("cls")
    dias_semana = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
    total = 0
    for dia in dias_semana:
        venta = float(input(f"Ingrese las ventas del dia {dia}: "))
        total += venta

    print(f"El total de venta semanal es: {total}")


def recepcionCafe():
    ##Tu misión: Una cooperativa recibe 5 sacos. Solicita el peso de cada uno, muestra su número de recepción y calcula el peso total.
    os.system("cls")
    print("-"*5 + " REVISION DE PESO DE SACO " + "-"*5)
    total = 0 
    for saco in range(5):
        peso_saco = float(input(f"Ingrese el peso del saco #{saco+1}: "))
        total += peso_saco

    print(f"El peso total de los cinco sacos es igual a {total}")


def revisionInventario():
    ##Tu misión: Una distribuidora revisa 8 productos. Solicita nombre y existencia; muestra los que tienen menos de 10 unidades y cuenta las alertas.
    os.system("cls")
    alertas = 0
    print("-"*5 + " BIENVENIDO A LA DISTRIBUIDORA " + "-"*5)
    for i in range(8):
        nombre = input("Ingrese el nombre del producto: ")
        existencia = int(input("Ingrese la existencia: "))  

        if existencia < 10:
            print(f"⚠️ALERTA: {nombre} tiene solo {existencia} unidades.")
            alerta += 1 

    print(f"Cantidad de alertas: {alertas}")

def produccionPan():
    ##Tu misión: Una panadería registra durante 6 días la producción y las ventas. Calcula totales y producto sobrante.
    os.system("cls")
    print("-"*5 + " PRODUCCION DE PAN " + "-"*5)

    total_produccion = 0
    total_ventas = 0

    for dia in range(6):
        print(f"\nDia #{dia+1}")
        produccion = int(input("Ingrese la cantidad de panes producidos: "))
        ventas = int(input("Ingrese la cantidad de panes vendidos: "))

        total_produccion += produccion
        total_ventas += ventas

    sobrante = total_produccion - total_ventas

    print(f"\nTotal de panes producidos: {total_produccion}")
    print(f"Total de panes vendidos: {total_ventas}")
    print(f"Total de panes sobrantes: {sobrante}")

def evaluacionServicio():
    ##Tu misión: Un restaurante recoge 10 calificaciones entre 1 y 5. Calcula el promedio y cuenta cuántas fueron 4 o 5.
    os.system("cls")
    print("-"*5 + " EVALUACION DEL SERVICIO " + "-"*5)

    total = 0
    valoraciones_altas = 0

    for i in range(10):
        calificacion = int(input(f"Ingrese la calificacion #{i+1} entre 1 y 5: "))
        total += calificacion

        if calificacion == 4 or calificacion == 5:
            valoraciones_altas += 1

    promedio = total / 10

    print(f"El promedio de las calificaciones es: {promedio}")
    print(f"Cantidad de valoraciones de 4 o 5: {valoraciones_altas}")