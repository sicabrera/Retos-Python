import os

from excepciones import conversionEdad
from excepciones import divisionSegura
from excepciones import accesoLista
from excepciones import consultaCliente
from excepciones import cierreGarantizado
from excepciones import precioProducto
from excepciones import cantidadProductos
from excepciones import calificacion
from excepciones import edadRegistro
from excepciones import tresEntradas
from excepciones import promedioVentas
from excepciones import descuentoProporcional
from excepciones import conversionMoneda
from excepciones import tiposIncompatibles
from excepciones import calculoComision
from excepciones import indiceInventario
from excepciones import diccionarioEmpleados
from excepciones import menuOpciones
from excepciones import archivoReportes
from excepciones import importacionControlada


def main():
    os.system("cls")
    opc = 0

    while (opc != 99):
        print("-" * 50)
        print("******** CATALOGO DE FUNCIONES ********")
        print("1..............Conversion de edad")
        print("2..............Division segura")
        print("3..............Acceso a una lista")
        print("4..............Consulta de cliente")
        print("5..............Cierre garantizado")
        print("6..............Precio de un producto")
        print("7..............Cantidad de productos")
        print("8..............Calificacion")
        print("9..............Edad para registro")
        print("10.............Tres entradas consecutivas")
        print("11.............Promedio de ventas")
        print("12.............Descuento proporcional")
        print("13.............Conversion de moneda")
        print("14.............Tipos incompatibles")
        print("15.............Calculo de comision")
        print("16.............Indice de inventario")
        print("17.............Diccionario de empleados")
        print("18.............Menu de opciones")
        print("19.............Archivo de reportes")
        print("20.............Importacion controlada")
        print("99.............Terminar")
        print("-" * 50)

        opc = int(input("Seleccione la tarea a ejecutarse: "))

        match opc:
            case 1:
                conversionEdad()
            case 2:
                divisionSegura()
            case 3:
                accesoLista()
            case 4:
                consultaCliente()
            case 5:
                cierreGarantizado()
            case 6:
                precioProducto()
            case 7:
                cantidadProductos()
            case 8:
                calificacion()
            case 9:
                edadRegistro()
            case 10:
                tresEntradas()
            case 11:
                promedioVentas()
            case 12:
                descuentoProporcional()
            case 13:
                conversionMoneda()
            case 14:
                tiposIncompatibles()
            case 15:
                calculoComision()
            case 16:
                indiceInventario()
            case 17:
                diccionarioEmpleados()
            case 18:
                menuOpciones()
            case 19:
                archivoReportes()
            case 20:
                importacionControlada()
            case 99:
                print("Saliendo...")
            case _:
                print("Opcion no valida.")


main()