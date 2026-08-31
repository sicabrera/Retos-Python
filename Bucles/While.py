import os


def cierreCaja():
    ##Tu misión: Ingresa los montos de ventas hasta escribir 0. Calcula el total recaudado y la cantidad de ventas.
    os.system("cls")
    print("-"*5 + " CIERRE DE CAJA " + "-"*5)

    total = 0
    cantidad_ventas = 0

    venta = float(input("Ingrese el monto de la venta (0 para terminar): "))

    while venta != 0:
        total += venta
        cantidad_ventas += 1

        venta = float(input("Ingrese el monto de la venta (0 para terminar): "))

    print(f"Total recaudado: {total}")
    print(f"Cantidad de ventas: {cantidad_ventas}")


def accesoSistema():
    ##Tu misión: Solicita la clave hasta que sea correcta. Cuenta los intentos e informa cuántos fueron necesarios.
    os.system("cls")
    print("-"*5 + " ACCESO AL SISTEMA " + "-"*5)

    clave_correcta = "1234"
    clave = ""
    intentos = 0

    while clave != clave_correcta:
        clave = input("Ingrese la clave: ")
        intentos += 1

        if clave != clave_correcta:
            print("Clave incorrecta.")

    print("Acceso permitido.")
    print(f"Cantidad de intentos: {intentos}")


def cantidadPedido():
    ##Tu misión: Un distribuidor acepta de 1 a 100 unidades. Solicita la cantidad hasta que sea válida y luego calcula el total.
    os.system("cls")
    print("-"*5 + " CANTIDAD DE PEDIDO " + "-"*5)

    cantidad = int(input("Ingrese la cantidad de unidades: "))

    while cantidad < 1 or cantidad > 100:
        print("Cantidad no valida. Debe ser entre 1 y 100.")
        cantidad = int(input("Ingrese nuevamente la cantidad: "))

    precio = float(input("Ingrese el precio por unidad: "))
    total = cantidad * precio

    print(f"Cantidad solicitada: {cantidad}")
    print(f"Total a pagar: {total}")


def combustibleReparto():
    ##Tu misión: Una motocicleta inicia con 8 litros. Registra el consumo de cada recorrido mientras quede combustible y alerta al llegar a 1 litro.
    os.system("cls")
    print("-"*5 + " COMBUSTIBLE DE REPARTO " + "-"*5)

    combustible = 8

    while combustible > 1:
        print(f"Combustible disponible: {combustible} litros")
        consumo = float(input("Ingrese el consumo del recorrido: "))

        if consumo > 0 and consumo <= combustible:
            combustible -= consumo
        else:
            print("Consumo no valido.")

    print(f"Combustible restante: {combustible} litros")
    print("⚠️ ALERTA: El combustible ha llegado a 1 litro o menos.")


def reposicionExistencias():
    ##Tu misión: Una tienda tiene 3 unidades y desea llegar a 20. Solicita cada reposición y termina al alcanzar o superar la meta.
    os.system("cls")
    print("-"*5 + " REPOSICION DE EXISTENCIAS " + "-"*5)

    existencia = 3

    while existencia < 20:
        print(f"Existencia actual: {existencia}")
        reposicion = int(input("Ingrese la cantidad a reponer: "))

        if reposicion > 0:
            existencia += reposicion
        else:
            print("La cantidad debe ser mayor que 0.")

    print(f"Existencia final: {existencia}")
    print("Meta alcanzada.")