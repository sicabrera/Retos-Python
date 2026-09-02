import os


def conversionEdad():
    os.system("cls")
    ##Tu misión: Una aplicación solicita la edad. Si la persona escribe texto que no representa un entero, debe mostrar un mensaje claro y continuar sin finalizar abruptamente.
    try: 
        edad = int(input("Ingresa tu edad: "))
    except ValueError:
        print("Error: ingrese un número entero.")
    else:
        print(f'Edad: {edad}')


def divisionSegura():
    os.system("cls")
    try:
        dividendo = float(input("Dividendo: "))
        divisor = float(input("Divisor: "))
        resultado = dividendo / divisor
    except ValueError:
        print("Error: ingrese valores numéricos.")
    except ZeroDivisionError:
        print("Error: el divisor no puede ser cero.")
    else:
        print("Resultado:", resultado)
    finally:
        print("Operación finalizada.")


def accesoLista():
    os.system("cls")
    ##Tu misión: Una aplicación guarda nombres en una lista y solicita una posición. Controla el caso en que la posición no exista.
    nombres = []

    for i in range(3):
        nombre = input(f'Ingrese el nombre #{i+1}: ')
        nombres.append(nombre)

    try:
        posicion = int(input("Ingrese la posicion que desea consultar: "))
        print(nombres[posicion])
    except ValueError:
        print("Error: ingrese un numero entero.")
    except IndexError:
        print("Error: esa posicion no existe.")


def consultaCliente():
    os.system("cls")
    cliente = {
        "nombre": "María",
        "telefono": "8888-8888"
    }

    try: 
        clave = input("Dato a consultar: ")
        print(cliente[clave])
    except KeyError: 
        print("Ese dato no esta registrado")


def cierreGarantizado():
    os.system("cls")
    ##Tu misión: Simula una operación que puede fallar y utiliza finally para mostrar un mensaje que siempre debe aparecer al terminar el proceso.
    print("SUMA DE ENTEROS")

    try:
        numero1 = int(input("Numero #1: "))
        numero2 = int(input("Numero #2: "))
        resultado = numero1 + numero2
    except ValueError:
        print("Error: ingrese un numero entero.")
    else:
        print("Resultado:", resultado)
    finally:
        print("Operación finalizada.")


def precioProducto():
    os.system("cls")

    try: 
        precio = float(input("Ingrese el precio del producto: "))
    except ValueError:
        print("Ingrese un valor numerico.")
    finally: 
        print("Operacion finalizada")


def cantidadProductos():
    os.system("cls")
    ##Tu misión: Solicita la cantidad de unidades que una persona desea comprar. Controla entradas que no puedan convertirse a entero.

    try:
        cantidad = int(input("Ingrese la cantidad de productos: "))
    except ValueError:
        print("Error: ingrese un numero entero.")
    else:
        print(f"Cantidad de productos: {cantidad}")


def calificacion():
    os.system("cls")
    ##Tu misión: Solicita una calificación numérica. Controla ValueError y, si la conversión funciona, indica si la calificación está entre 0 y 100.

    try:
        nota = float(input("Ingrese la calificacion: "))
    except ValueError:
        print("Error: ingrese un valor numerico.")
    else:
        if nota >= 0 and nota <= 100:
            print("La calificacion esta entre 0 y 100.")
        else:
            print("La calificacion esta fuera del rango.")


def edadRegistro():
    os.system("cls")
    ##Tu misión: Solicita la edad. Controla ValueError y evita que el programa continúe con una edad que no sea válida.

    try:
        edad = int(input("Ingrese su edad: "))
    except ValueError:
        print("Error: la edad debe ser un numero entero.")
    else:
        if edad >= 0 and edad <= 120:
            print(f"Edad registrada: {edad}")
        else:
            print("Error: la edad no es valida.")


def tresEntradas():
    os.system("cls")
    ##Tu misión: Solicita nombre, edad y salario. Controla únicamente las conversiones que pueden producir excepciones y muestra qué dato debe corregirse.

    nombre = input("Ingrese su nombre: ")

    try:
        edad = int(input("Ingrese su edad: "))
    except ValueError:
        print("Error: debe corregir la edad.")
        return

    try:
        salario = float(input("Ingrese su salario: "))
    except ValueError:
        print("Error: debe corregir el salario.")
        return

    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Salario: {salario}")


def promedioVentas():
    os.system("cls")
    ##Tu misión: Solicita tres ventas y calcula su promedio. Controla ValueError y ZeroDivisionError.

    try:
        venta1 = float(input("Ingrese la venta #1: "))
        venta2 = float(input("Ingrese la venta #2: "))
        venta3 = float(input("Ingrese la venta #3: "))

        cantidad = 3
        promedio = (venta1 + venta2 + venta3) / cantidad

    except ValueError:
        print("Error: ingrese valores numericos.")
    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero.")
    else:
        print(f"Promedio de ventas: {promedio}")


def descuentoProporcional():
    os.system("cls")
    ##Tu misión: Calcula un porcentaje a partir de un monto y una base. Controla entradas no numéricas y una base igual a cero.

    try:
        monto = float(input("Ingrese el monto: "))
        base = float(input("Ingrese la base: "))

        porcentaje = (monto / base) * 100

    except ValueError:
        print("Error: ingrese valores numericos.")
    except ZeroDivisionError:
        print("Error: la base no puede ser cero.")
    else:
        print(f"Porcentaje: {porcentaje}%")


def conversionMoneda():
    os.system("cls")
    ##Tu misión: Solicita monto y tasa de cambio. Calcula el equivalente y controla los errores de conversión.

    try:
        monto = float(input("Ingrese el monto: "))
        tasa = float(input("Ingrese la tasa de cambio: "))

        equivalente = monto * tasa

    except ValueError:
        print("Error: ingrese valores numericos.")
    else:
        print(f"Equivalente: {equivalente}")


def tiposIncompatibles():
    os.system("cls")
    ##Tu misión: Provoca TypeError y después corrígelo mediante una conversión.

    numero = 10
    texto = "5"

    try:
        resultado = numero + texto
    except TypeError:
        print("Error: no se puede sumar un numero con una cadena.")

        texto = int(texto)
        resultado = numero + texto

        print(f"Resultado corregido: {resultado}")


def calculoComision():
    os.system("cls")
    ##Tu misión: Calcula una comisión a partir de ventas y porcentaje. Usa try/except para controlar datos no numéricos.

    try:
        ventas = float(input("Ingrese el total de ventas: "))
        porcentaje = float(input("Ingrese el porcentaje de comision: "))

        comision = ventas * porcentaje / 100

    except ValueError:
        print("Error: ingrese valores numericos.")
    else:
        print(f"Comision: {comision}")


def indiceInventario():
    os.system("cls")
    ##Tu misión: Crea una lista de productos y solicita una posición. Controla IndexError y ValueError con mensajes diferentes.

    productos = ["Arroz", "Leche", "Pan", "Cafe"]

    print(productos)

    try:
        posicion = int(input("Ingrese una posicion (0 - 3): "))
        print(f"Producto: {productos[posicion]}")

    except ValueError:
        print("Error: debe ingresar un numero entero.")
    except IndexError:
        print("Error: esa posicion no existe.")


def diccionarioEmpleados():
    os.system("cls")
    ##Tu misión: Consulta información de un empleado mediante una clave. Controla KeyError.

    empleado = {
        "nombre": "Carlos",
        "edad": 25,
        "cargo": "Vendedor"
    }

    try:
        clave = input("Ingrese el dato que desea consultar: ")
        print(empleado[clave])
    except KeyError:
        print("Error: ese dato no existe.")


def menuOpciones():
    os.system("cls")
    ##Tu misión: Solicita una opción numérica para un menú. Controla ValueError y usa else.

    print("1. Agregar")
    print("2. Consultar")
    print("3. Salir")

    try:
        opcion = int(input("Seleccione una opcion: "))
    except ValueError:
        print("Error: debe ingresar un numero.")
    else:
        if opcion == 1:
            print("Selecciono Agregar.")
        elif opcion == 2:
            print("Selecciono Consultar.")
        elif opcion == 3:
            print("Selecciono Salir.")
        else:
            print("Opcion no valida.")


def archivoReportes():
    os.system("cls")
    ##Tu misión: Intenta abrir un archivo llamado reportes.txt. Controla FileNotFoundError y utiliza finally.

    try:
        with open("reportes.txt", "r") as archivo:
            contenido = archivo.read()
            print(contenido)

    except FileNotFoundError:
        print("Error: el archivo reportes.txt no existe.")
    finally:
        print("Operacion finalizada.")


def importacionControlada():
    os.system("cls")
    ##Tu misión: Simula la importación de un módulo que no existe y controla ModuleNotFoundError.

    try:
        import modulo_inexistente
    except ModuleNotFoundError:
        print("Error: el modulo no existe.")
        print("Revise el nombre del modulo o verifique que este instalado.")