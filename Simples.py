import os 
os.system("cls")


def inventarioPulperia():
    print("********** PULPERIA DE LA ESQUINA 🏠 **********")
    producto = input("Ingrese el nombre del producto: ")
    stock = int(input("Cuantas unidades hay en existencia?: "))

    if stock < 5:
        print("⚠️⚠️⚠️ ALERTA!! ⚠️⚠️⚠️")
        print(f"\nSe necesita reponer este producto: {producto}")

    else: 
        print("Producto ingresado exitosamente")

def promocionTienda():
    #Una tienda de Masaya aplica una promoción simulada de 10% cuando la compra supera C$1,500. Solicita el monto y muestra el total.
    print("********** TIENDA MASAYA 🐒 **********")

    monto = int(input("Ingrese el monto de su compra: "))
    descuento = 0.10
    if monto > 1500:
        total = monto - (monto * descuento)
        print(f"FELICIDADES!!! SE LE APLICÓ UN DESCUENTO DE {descuento * 100}")

    else: 
        print("No se le aplicó descuento.")
        total = monto


    print(f"El total a pagar es: {total}")

def metaVentas():
    #Tu misión: Un emprendimiento fija una meta diaria de C$4,000. Lee el total vendido e informa si se alcanzó; muestra cuánto faltó o cuánto se superó.

    meta_diaria = 4000.00
    total = float(input("Ingrese el total diario vendido: "))
    if total > meta_diaria:
        print("🎉🎉 FELICIDADES 🎉🎉")
        print(f"Han cumplido con la meta diaria de C${meta_diaria}.")

    else: 
        print(f"No han cumplido con la meta diaria de ventas \nHizo falta C${meta_diaria - total} para llegar a la meta diaria de c${meta_diaria}")

def entregaComedor():
    print("👏 BIENVENIDOS AL COMEDOR EL CUADRA 👏")
    pedido = float(input("Ingrese el total de la comida "))
    recargo_envio = 40.0
    if pedido < 300:
        total = pedido + recargo_envio
        print(f"⚠️ Se le cobrara un recargo de {recargo_envio} \nEl total a pagar sería de {total}")

    else: 
        print(f"✅ FELICIDADES ENVIO GRATIS \nEl total a pagar sería de {total}")

def pesoProductos():
    #Una bodega espera sacos de 46 kg. Lee el peso e informa si cumple o debe revisarse por estar debajo del valor esperado.
    print("🚨 REVISION DE PESO DE SACO 🚨")
    peso_saco = float(input("Ingrese el peso en kilogramos del saco: "))
    if peso_saco < 46: 
        print("❌❌❌ NO CUMPLE CON EL PESO MINIMO DE 46 KG, FAVOR REVISAR EL SACO ❌❌❌")
    else:
        print("✅✅✅ EL SACO CUMPLE CON EL PESO MINIMO DE 46 KG ✅✅✅")

inventarioPulperia()
promocionTienda()
metaVentas()
entregaComedor()
pesoProductos()