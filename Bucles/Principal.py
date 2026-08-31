import os

from For import ventasMinisuper, recepcionCafe, revisionInventario, produccionPan, evaluacionServicio
from While import cierreCaja, accesoSistema, cantidadPedido, combustibleReparto, reposicionExistencias


opcion = 0

while opcion != 11:
    os.system("cls")

    print("-"*10 + " MENU PRINCIPAL " + "-"*10)
    print("1. Ventas del minisuper")
    print("2. Recepcion de cafe")
    print("3. Revision de inventario")
    print("4. Produccion de pan")
    print("5. Evaluacion del servicio")
    print("6. Cierre de caja")
    print("7. Acceso al sistema")
    print("8. Cantidad de un pedido")
    print("9. Combustible de reparto")
    print("10. Reposicion de existencias")
    print("11. Salir")
    print("-"*36)

    opcion = int(input("Seleccione una opcion: "))

    if opcion == 1:
        ventasMinisuper()

    elif opcion == 2:
        recepcionCafe()

    elif opcion == 3:
        revisionInventario()

    elif opcion == 4:
        produccionPan()

    elif opcion == 5:
        evaluacionServicio()

    elif opcion == 6:
        cierreCaja()

    elif opcion == 7:
        accesoSistema()

    elif opcion == 8:
        cantidadPedido()

    elif opcion == 9:
        combustibleReparto()

    elif opcion == 10:
        reposicionExistencias()

    elif opcion == 11:
        print("Saliendo del programa...")

    else:
        print("Opcion no valida.")

    if opcion != 11:
        input("\nPresione ENTER para regresar al menu...")