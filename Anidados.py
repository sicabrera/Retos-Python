import os
os.system("cls")


def creditoInterno():
    # Una pulpería vende al crédito sólo a clientes registrados.
    # Si lo están, revisa que su saldo pendiente no supere C$500.

    print("********** PULPERIA - CREDITO INTERNO 🏠 **********")

    registrado = input("¿El cliente está registrado? (SI/NO): ").upper()

    if registrado in ["S", "SI", "YES", "Y", "VERDADERO", "TRUE", "V", "T", "1"]:
        saldo = float(input("Ingrese el saldo pendiente del cliente: C$"))

        if saldo <= 500:
            print("✅ CREDITO APROBADO")
            print(f"El cliente tiene un saldo pendiente de C${saldo}")
        else:
            print("❌ CREDITO DENEGADO")
            print(f"El cliente supera el saldo máximo permitido de C$500.")
    else:
        print("❌ CREDITO DENEGADO")
        print("El cliente no se encuentra registrado.")


def servicioEntrega():
    # La tarifa depende de la zona y luego del peso del paquete.

    print("\n********** SERVICIO DE ENTREGA 📦 **********")

    zona = input("Ingrese la zona de entrega (urbana/rural): ").lower()
    peso = float(input("Ingrese el peso del paquete en kg: "))

    if zona == "urbana":
        tarifa = 60

        if peso > 5:
            tarifa = tarifa + 30
            print("⚠️ Se agregó un recargo de C$30 por superar los 5 kg.")

        print(f"El total del envío es de C${tarifa}")

    else:
        if zona == "rural":
            tarifa = 100

            if peso > 5:
                tarifa = tarifa + 50
                print("⚠️ Se agregó un recargo de C$50 por superar los 5 kg.")

            print(f"El total del envío es de C${tarifa}")

        else:
            print("❌ Zona ingresada no válida.")


def clasificacionCafe():
    # Primero se verifica que la humedad esté entre 10% y 12%.
    # Si cumple, se clasifica según la cantidad de defectos.

    print("\n********** CLASIFICACION DE CAFE ☕ **********")

    humedad = float(input("Ingrese el porcentaje de humedad del lote: "))

    if humedad >= 10 and humedad <= 12:
        print("✅ El nivel de humedad es adecuado.")

        defectos = int(input("Ingrese la cantidad de defectos encontrados: "))

        if defectos <= 3:
            print("☕ Clasificación: CAFE PREMIUM")

        else:
            if defectos <= 7:
                print("☕ Clasificación: CAFE ESTANDAR")

            else:
                print("☕ Clasificación: CAFE COMERCIAL")

    else:
        print("❌ El lote no cumple con el nivel de humedad requerido.")
        print("La humedad debe estar entre 10% y 12%.")


def reservaHospedaje():
    # La promoción solamente se aplica durante temporada baja.
    # Si la reserva alcanza 3 noches recibe un descuento mayor.

    print("\n********** HOSPEDAJE GRANADA 🏨 **********")

    temporada = input("¿La reserva es en temporada baja? (si/no): ").lower()

    if temporada == "si":
        noches = int(input("Ingrese la cantidad de noches: "))
        precio_noche = float(input("Ingrese el precio por noche: C$"))

        subtotal = noches * precio_noche

        if noches >= 3:
            descuento = 0.20
        else:
            descuento = 0.10

        total = subtotal - (subtotal * descuento)

        print(f"🎉 Se aplicó un descuento del {descuento * 100}%")
        print(f"Subtotal: C${subtotal}")
        print(f"Total a pagar: C${total}")

    else:
        noches = int(input("Ingrese la cantidad de noches: "))
        precio_noche = float(input("Ingrese el precio por noche: C$"))

        total = noches * precio_noche

        print("No se aplica promoción porque no es temporada baja.")
        print(f"Total a pagar: C${total}")


def ventaFerreteria():
    # La ferretería distingue entre clientes mayoristas y minoristas.
    # Cada tipo tiene un monto mínimo diferente para obtener descuento.

    print("\n********** FERRETERIA 🔨 **********")

    tipo_cliente = input("Ingrese el tipo de cliente (mayorista/minorista): ").lower()
    monto = float(input("Ingrese el monto de la compra: C$"))

    if tipo_cliente == "mayorista":

        if monto >= 5000:
            descuento = 0.15
            total = monto - (monto * descuento)

            print("🎉 DESCUENTO MAYORISTA APLICADO")
            print(f"Descuento: {descuento * 100}%")
            print(f"Total a pagar: C${total}")

        else:
            print("No alcanza el mínimo de C$5000 para el descuento mayorista.")
            print(f"Total a pagar: C${monto}")

    else:
        if tipo_cliente == "minorista":

            if monto >= 1500:
                descuento = 0.08
                total = monto - (monto * descuento)

                print("🎉 DESCUENTO MINORISTA APLICADO")
                print(f"Descuento: {descuento * 100}%")
                print(f"Total a pagar: C${total}")

            else:
                print("No alcanza el mínimo de C$1500 para el descuento minorista.")
                print(f"Total a pagar: C${monto}")

        else:
            print("❌ Tipo de cliente no válido.")


creditoInterno()
servicioEntrega()
clasificacionCafe()
reservaHospedaje()
ventaFerreteria()