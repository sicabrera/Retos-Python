import os 
from Simples import inventarioPulperia 
from Simples import promocionTienda
from Simples import metaVentas
from Simples import entregaComedor
from Simples import pesoProductos


def main():
    os.system("cls")
    print("-"*50)
    print("******** CATALOGO DE FUNCIONES ********")
    print("1..............Inventario de una pulpería")
    print("2..............Promoción de una tienda")
    print("3..............Meta de ventas")
    print("4..............Entrega de un comedor")
    print("5..............Peso de productos")
    print("6..............Terminar")
    print("-"*50)
    opc = int(input("Seleccione la tarea a ejecutarse: "))

    match opc: 
        case 1: 
            return inventarioPulperia()
        case 2: 
            return promocionTienda()
        case 3: 
            return metaVentas()
        case 4: 
            entregaComedor()
        case 5: 
            pesoProductos()
        case 6: 
            return print("Saliendo...")
        case _:
            return print("Opcion invalida")
    
main()

""" os.system("cls")
    #La variable nombre_producto es de tipo str 
    nombre_producto = input("Digite el nombre de su producto: ")

    #La variable precio es de tipo float
    precio = float(input("Digite el precio del producto: "))

    #La variable cantidad_comprada es de tipo int 
    cantidad_comprada = int(input("Digite la cantidad comprada del producto: "))

    #La variable descuento es de tipo bool 
    respuesta = input("El producto tiene descuento S/N?: ").strip().upper()
    descuento = respuesta in ["S", "SI", "YES", "Y", "VERDADERO", "TRUE", "V", "T", "1"]


    print("=== RESUMEN DE FACTURACION ===")

    print(f"Producto: {nombre_producto}")
    print(f"Precio: {precio}")
    print(f"Cantidad: {cantidad_comprada}")
    print(f"Descuento: {descuento}") """